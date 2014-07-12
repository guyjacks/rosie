import rosie.rosie as rosie

def test_base(callback_mock):
    state = rosie.State('one')
    t = rosie.Transition(state.state_name, 'two', callback_mock, 'arg1', 'arg2')
    state.add_transition('next', t)
    actual = state.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = callback_mock
    assert expected_callback == actual.callback
    expected_callback_args = 'arg1', 'arg2'
    assert expected_callback_args == actual.callback_args

def test_empty_callback():
    assert True == False
