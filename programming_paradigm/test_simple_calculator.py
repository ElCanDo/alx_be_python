import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5) # check if 2 + 3 = 5
        self.assertEqual(self.calc.add(-1, 1), 0) # check if -1 + 1 = 0
        self.assertEqual(self.calc.add(0, 1), 1) # check if 0 + 1 = 1
        self.assertEqual(self.calc.add(0, 0), 0) # check if 0 + 0 = 0
       

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(3, 2), 1) # Check if 3 - 2 = 1
        self.assertEqual(self.calc.subtract(-1, 1), -2) # Check if -1 -1 = -2
        self.assertEqual(self.calc.subtract(2, 0), 2) # check if 2 - 0 = 2
        self.assertEqual(self.calc.subtract(1, 1), 0) # check if 1 - 1 = 0

    def test_mutltiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6) # check if 2 * 3 = 6 
        self.assertEqual(self.calc.multiply(-2, 1), -2) # check if -2 * 1 = -2
        self.assertEqual(self.calc.multiply(0, 1), 0) # check if 0 + 1 = 0
    
    def test_divide(self):
        """Test the division method."""
        self.assertAlmostEqual(self.calc.divide(15, 3), 5.0) # check if -1 + 1 = 0
        self.assertAlmostEqual(self.calc.divide(-9, 3), -3.0) # check if -1 + 1 = 0
        self.assertAlmostEqual(self.calc.divide(20, 3), 6.66666667, places=5) # check for floating-point  division
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)      # Check for division by zero. 

if __name__ == "__main__":
    unittest.main()
