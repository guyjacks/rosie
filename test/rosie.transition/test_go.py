import rosie.rosie as rosie
def test_base():
    t = rosie.Transition('one')
    t.go('two')
    expected = 'two'
    assert expected == t.next
