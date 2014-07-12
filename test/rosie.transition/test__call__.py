import rosie.rosie as rosie
def test_base(callback_mock):
    t = rosie.Transition('one', 'two', callback_mock, 'arg1', 'arg2')
    actual = t()
    expected = 'two'
    assert expected == actual
    callback_mock.assert_called_with('arg1', 'arg2', start_state_name='one', destination_state_name='two')

def test_without_callback():
    t = rosie.Transition('one', 'two')
    actual = t()
    expected = 'two'
    assert expected == actual

def test_without_next_specified():
    t = rosie.Transition('one')
    actual = t()
    # expect an error to be raised
    assert True == False
