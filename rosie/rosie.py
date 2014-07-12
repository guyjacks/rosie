class FiniteStateMachine(object):
    def __init__(self, initial_state_name=""):
        self.initial_state_name = initial_state_name
        self.started = False
        self.current_state_obj = ""
        self.history = []
        #self.final_states = set([initial_state_name])

    def set_current_state_obj(self, state_name, is_terminal=False):
        # REFACTOR - throw error if state is not a valid state name
        if not is_terminal:
            self.current_state_obj = self.__dict__[state_name]
        else:
            self.current_state_obj = State(state_name)

    def __getattr__(self, name):
        state_obj = State(name)
        # REFACTOR - throw error if state name is using one of the reserved keys
            ## self.initial_state for example cannot be the name of a state
        # REFACTOR - override functionality for setting and getting the other object attributes
            ## may use other built-ins like __get__ or whatever
        # REFACTOR - block duplicate states or throw an error
        setattr(self, name, state_obj)
        return state_obj
        
    def __str__(self):
        ret = ""
        for state_name, state_obj in self.__dict__.iteritems():
            # Not all of the members are States so need to check type before printing
            if type(state_obj) is State:
                ret += str(state_obj) + '\n'
        return ret

    def current_state_is_set(self):
        return self.initial_state_name == ""

    def set_initial_state_name(self, state_name=""):
        # REFACTOR - try to use @property
        self.initial_state_name = state_name

    def state_exists(self, state_name):
        return state_name in self.__dict__

    def start(self):
        # REFACTOR - Throw error if initial state name has not been set
        # REFACTOR - block user from calling this function directly
        # REFACTOR - do not start state machine if its already been started
        # REFACTOR - throw error if initial state name is not a valid state name
        self.set_current_state_obj(self.initial_state_name) 
        self.started = True

    def transition(self, event):
        """ show examples for class function callbacks since beginners are always going to ask this question"""
        if not self.started:
            self.start()

        if self.current_state_obj.is_valid_transition(event):
            # transition is a callable
            transition = self.current_state_obj.get_transition(event)
            # if the a callable was registered on this transition
            # then transition() will call it
            # the next state name is always returned
            next_state_name = transition()
            
            # keep track of transition history
            record = (self.current_state_obj.state_name, event, next_state_name)
            self.history.append(record)
            
            # Set the new current state
            if self.state_exists(next_state_name):
                self.set_current_state_obj(next_state_name)
            else:
                # The transition was valid but the target state was 
                # not explicitly created by the client.  This scenario 
                # implies that the target state is a terminal state.
                # I.E. fsm.y.next = z ...  The client does not have to 
                # create the z state since its the last state.
                self.set_current_state_obj(next_state_name, True)

            return next_state_name
        else:
            # REFACTOR - throw invalid transition error
            pass

class State(object):
    def __init__(self, state_name):
        self.state_name = state_name

    def __setattr__(self, attribute, value):
        # unreserved attribute names are transition names
        reserved_attribute_names = set(['state_name'])
        if attribute not in reserved_attribute_names:
            # attribute is a transition name
            if isinstance(value, basestring):
                # the client passed a string for state
                # i.e. fsm.state.next = state
                # attribute is the event
                # value is the target state of the transition
                t = Transition(self.state_name, value)
            else:
                # the client passed a tuple indicating a callback
                # i.e. fsm.state.next = state_name, callback, arg1, arg2
                if len(value) == 2:     
                    # the client passed a callback w/o any args
                    # i.e. fsm.state.next = state_name, callback
                    destination_state_name, callback = value
                    t = Transition(self.state_name, destination_state_name, callback)
                elif len(value) > 2:
                    # the client passed a callback w/ args
                    # i.e. fsm.state.next = state_name, callback, arg1, arg2
                    list_values = list(value)
                    destination_state_name = value[0]
                    callback = value[1]
                    callback_args = value[2:]
                    t = Transition(self.state_name, destination_state_name, callback, *callback_args)
            self.add_transition(attribute, t)
        else:
            # attribute is not a transition name
            # reserved attribute names should be treated normally
            self.__dict__[attribute] = value

    def add_transition(self, event, transition_obj):
        # state_name is reserved for holding the state's name
        # raise an exception is 'state_name' is passed as the value for transition
        self.__dict__[event] = transition_obj

    def on(self, event):
        t = Transition(self.state_name)
        self.add_transition(event, t)
        return t

    def get_transition(self, transition):
        return self.__dict__[transition]

    def is_valid_transition(self, transition):
        return True

    def __str__(self):
        str = self.state_name + '\n'
        for transition, destination_state_name in self.__dict__.iteritems():
            # state_name stores the name of the state so do not print it as a transition
            if transition != 'state_name':
                str += transition + '->' + destination_state_name + '\n'
        return str

class Transition(object):
    def __init__(self, start, next="", callback="", *args):
        self.start = start
        self.next = next
        self.callback = callback
        self.callback_args = args

    def go(self, state_name):
        self.next = state_name
        return self

    def do(self, callback, *args, **kwargs):
        """ **kwargs['pass_states'] can be set to True or False
            - if True then pass start_state_name and destination_state_name to callback
        """
        self.callback = callback
        self.callback_args = args
        self.pass_states = False
        if 'pass_states' in kwargs:
            self.pass_states = kwargs['pass_states']
        
    def __call__(self):
        if self.callback != "":
            if self.pass_states:
                self.callback(*self.callback_args, start_state_name=self.start, destination_state_name=self.next)
            else:
                self.callback(*self.callback_args)
        return self.next
