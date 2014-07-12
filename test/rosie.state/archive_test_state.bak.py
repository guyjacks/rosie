import unittest
import fsm

class TestInit(unittest.TestCase):
    def test_init(self):
        expected = 'Some State Name'
        state = fsm.State(expected)
        actual = state.name
        self.assertEqual(actual, expected)

class TestBaseCases(unittest.TestCase):
    def setUp(self):
        self.state = fsm.State('colors')
        self.state.red = 'red'
        self.state.black = 'black'
        self.state.blue = 'blue'

    def test_str(self):
        output = str(self.state)
        expected = 'colors\n'
        self.assertIn(expected, output)
        
        expected = 'red->red\n'
        self.assertIn(expected, output)

        expected = 'black->black\n'
        self.assertIn(expected, output)

        expected = 'blue->blue\n'
        self.assertIn(expected, output)

    def test_str_does_not_print_state_name_as_transition(self):
        expected = 'colors->'
        self.assertNotIn(expected, str(self.state))

if __name__ == '__main__':
    unittest.main()
