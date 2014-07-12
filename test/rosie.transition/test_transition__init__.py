import rosie.rosie as rosie
def test_base(callback_mock):
    t = rosie.Transition('one')
    expected = 'one'
    assert expected == t.start

    t = rosie.Transition('one', 'two')
    expected = 'one'
    assert expected == t.start

    expected = 'two'
    assert expected == t.next

    t = rosie.Transition('one', 'two', callback_mock, 'arg1', 'arg2')
    expected = callback_mock
    assert expected == t.callback

    expected = 'arg1', 'arg2'
    assert expected == t.callback_args
