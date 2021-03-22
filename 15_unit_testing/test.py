import unittest
import main

"""
NOTES:
-----

- Unittest provides different assert methods, e.g., assertTrue

"""


class TestMain(unittest.TestCase):
    # Useful if I need to set up a couple of default functions.
    def setUp(self):
        print("about to test a function")

    def test_do_stuff(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        test_param = "shkshjs"
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")
    
    def test_do_stuff4(self):
        test_param = ""
        result = main.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")
    
    def test_do_stuff5(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 5)
    
    def tearDown(self):
        print("cleaning up")


if __name__ == '__main__':
    unittest.main()
