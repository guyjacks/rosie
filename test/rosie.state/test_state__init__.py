import rosie.rosie as rosie

def test_base():
    state = rosie.State('State One')
    expected = 'State One'
    assert state.state_name == expected
