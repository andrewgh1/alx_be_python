import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)
        # Add more assertions to thoroughly test the add method.
    
    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(2, 3), -1)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        # Add more assertions to thoroughly test the subtract method.

    def test_multiplication(self):
        """Tesst the multiplication method. """
        self.assertEqual(self.calc.multiply(2, 4), 8)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(0, 0), 0)
        # Add more assertions to thoroughly test the multiply method.
    
    def test_division(self):
        """Test the division method.""" 
        self.assertEqual(self.calc.divide(6, 3), 2)
        self.assertEqual(self.calc.divide(-6, 2), -3)
        self.assertEqual(self.calc.divide(-6, -2), 3)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(5, 0), None)  # Test division by zero
        # Add more assertions to thoroughly test the divide method.

if __name__ == '__main__':
    unittest.main()

#Running the test in the terminal: python -m unittest test_simple_calculator.py

    

