import unittest
import main
#Tests dont go into production, so the should easy to read not simpler
class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to test the function")
    def test_sum_1(self):
        '''HI'''
        test_param = 10
        result = main.sum_1(test_param)
        self.assertEqual(result,15)

    def test_sum_2(self):
        test_param = "asdsdsd"
        # result = main.sum_1(test_param)
        # self.assertIsInstance(result,ValueError)
        
    def test_sum_3(self):
        test_param = None
        # result = main.sum_1(test_param)
        # self.assertEqual(result,"Please enter a number")

    def test_sum_4(self):
        test_param = []
        # result = main.sum_1(test_param)
        # self.assertEqual(result,"Please enter a number")

    def tearDown(self):
        print("Cleaning up")

if __name__ == "__main__":
    unittest.main()
    #python -m unittest -v allows to run tests and see comments