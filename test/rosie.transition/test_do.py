import rosie.rosie as rosie
def test_pass_states_not_passed(callback_mock):
    t = rosie.Transition('one')
    t.do(callback_mock, 'arg1', 'arg2')
    expected = callback_mock
    assert expected == t.callback
    expected = 'arg1', 'arg2'
    assert expected == t.callback_args
    expected = False
    assert expected == t.pass_states

def test_pass_states_true(callback_mock):
    assert True == False

def test_pass_states_false(callback_mock):
    assert True == False
