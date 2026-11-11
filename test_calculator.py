import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(0, 3), 0)
        self.assertEqual(mul(2,0.5), 1)
        self.assertEqual(mul(1,3), 3)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(4,0), 0)
        self.assertAlmostEqual(div(3,1), 0.3)
        self.assertEqual(div(3, 6), 2)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
         div(0, 10)

    def test_logarithm(self):
        assert logarithm(2, 8) == 3
        assert logarithm(10, 100) == 2

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(0, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        with self.assertRaises(ValueError):
            hypotenuse(-1,2)
        with self.assertRaises(ValueError):
            hypotenuse(-2, -4)
        with self.assertRaises(ValueError):
            hypotenuse(5, -8)


    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(0), 0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
