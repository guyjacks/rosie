import rosie.rosie as rosie

def test_base():
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = 'two'
    fsm.two.next = 'three'
    fsm.three.next = 'four'
    expected = 'two'
    assert expected == fsm.transition('next')
    expected = 'three'
    assert expected == fsm.transition('next')
    expected = 'four'
    assert expected == fsm.transition('next')
    # Test transaction is being recorded properly
    assert True == False

def test_callback_with_pass_states_enabled_without_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = ('two', callback_mock)
    # pass states to the callback
    fsm.one.next.pass_states = True
    fsm.transition('next')
    # 'one' & 'two' expected because the callback is always passed the 
    # start state and end state of the transition
    callback_mock.assert_called_with(start_state_name='one', destination_state_name='two')

def test_callback_with_pass_states_enabled_with_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = ('two', callback_mock, 'arg1', 'arg2')
    fsm.one.next.pass_states = True
    fsm.transition('next')
    callback_mock.assert_called_with('arg1', 'arg2', start_state_name='one', destination_state_name='two')

def test_callback_with_pass_states_disabled_without_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = ('two', callback_mock)
    fsm.one.next.pass_states = False
    fsm.transition('next')
    assert () == callback_mock.call_args

def test_callback_with_pass_states_disabled_with_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = ('two', callback_mock, 'arg1', 'arg2')
    fsm.one.next.pass_states = False
    fsm.transition('next')
    assert (('arg1', 'arg2'), ) == callback_mock.call_args

def test_invalid_transition():
    assert True == False

def test_transition_from_terminal_state():
    assert True == False

def test_start_state_not_set():
    assert True == False

def test_invalid_callback():
    assert True == False
