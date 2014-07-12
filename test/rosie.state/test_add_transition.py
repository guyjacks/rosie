import rosie.rosie as rosie

def test_base(callback_mock):
    state = rosie.State('one')
    t = rosie.Transition(state.state_name, 'two', callback_mock, 'arg1', 'arg2')
    state.add_transition('next', t)
    actual  = state.get_transition('next')
    # actual should be a Transition object
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = callback_mock
    assert expected_callback == actual.callback
    expected_callback_args = 'arg1', 'arg2'
    assert expected_callback_args == actual.callback_args

def test_empty_callback():
    state = rosie.State('one')
    t = rosie.Transition(state.state_name, 'two')
    state.add_transition('next', t)
    actual = state.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = ""
    assert expected_callback == actual.callback
    expected_callback_args = ()
    assert expected_callback_args == actual.callback_args

def test_empty_destination_state_name():
    state = rosie.State('State One')
    assert True == False

def test_unallowed_transition_names():
    state = rosie.State('State one')
    # state_name is reserved in self.__dict__ for the state's name.
    # giving this name to a transition would create conflicts.
    assert True == False
