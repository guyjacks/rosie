import rosie.rosie as rosie

def test_without_callback():
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = 'two'

    actual = fsm.one.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = ""
    assert expected_callback == ""
    expected_callback_args = ()
    assert expected_callback_args == actual.callback_args

def test_callback_without_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
    fsm.one.next = ('two', callback_mock)
 
    actual = fsm.one.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = callback_mock
    assert expected_callback == actual.callback
    expected_callback_args = ()
    assert expected_callback_args == actual.callback_args

def test_callback_with_args(callback_mock):
    fsm = rosie.FiniteStateMachine('one')
#fsm.one.next = ('two', callback_mock, 'arg1', 'arg2')
    fsm.one.next = 'two', callback_mock, 'arg1', 'arg2'

    actual = fsm.one.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = callback_mock
    assert expected_callback == actual.callback
    expected_callback_args = 'arg1', 'arg2'
    assert expected_callback_args == actual.callback_args
