import unittest
import script


class TestMain(unittest.TestCase):
    def setup(self):
        print("testing function from random choice game")
    
    def test_input_wrong_guess(self):
        result = script.check_guess(5, 7)
        self.assertEqual(result, "wrong answer. try again.")
    
    def test_input_right_guess(self):
        result = script.check_guess(3, 3)
        self.assertEqual(result, "you are a genius!")
    
    def test_input_out_of_range(self):
        result = script.check_guess(33, 8)
        self.assertEqual(result, "Hey boludo, I said 1 to 10!")
    
    def test_input_value_error(self):
        result = script.play_game("error", 7)
        self.assertEqual(result, "please enter a number")

if __name__ == '__main__':
    unittest.main()