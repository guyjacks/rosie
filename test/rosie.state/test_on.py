import rosie.rosie as rosie
def test_base():
    state = rosie.State('one')
    transition = state.on('next')

    # test the transition was properly instantiated and returned
    expected_next_state = ""
    assert expected_next_state == transition.next
    expected_callback = ""
    assert expected_callback == transition.callback
    expected_callback_args = ()
    assert expected_callback_args == transition.callback_args

    # test the event was registered on the state
    actual = state.get_transition('next')
    assert expected_next_state == actual.next
    assert expected_callback == actual.callback
    assert expected_callback_args == actual.callback_args
