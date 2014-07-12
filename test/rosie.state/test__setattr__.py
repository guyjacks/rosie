import rosie.rosie as rosie

def test_base(callback_mock):
    state = rosie.State('one')
    expected = 'one'
    assert expected == state.state_name

    setattr(state, 'next', ('two', callback_mock, 'arg1', 'arg2'))
    actual = state.get_transition('next')
    expected_next_state = 'two'
    assert expected_next_state == actual.next
    expected_callback = callback_mock
    assert expected_callback == actual.callback
    expected_callback_args = 'arg1', 'arg2'
    assert expected_callback_args == actual.callback_args
