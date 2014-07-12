from rosie import rosie

def test_base():
    state = rosie.State('State One')
    actual = str(state)
    
    expected = "State One\n"
    assert expected in actual
