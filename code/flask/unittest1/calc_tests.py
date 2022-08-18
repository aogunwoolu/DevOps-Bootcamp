import unittest
import calc

class TestCalc(unittest.TestCase):
    """Test methods needed to start tests"""

    def test_add(self):
        # Triple A pattern:
        # 1. Arrange
        # 2. Act
        # 3. Assert

        result = calc.add(10, 5)
        self.assertEqual(result, 15)

    def test_subtract(self):
        self.assertEqual(calc.subtract(2,1), 1)

    def test_subtract_three_minus_one(self):
        res = calc.subtract(3, 1)
        self.assertEqual(res, 2)

    def test_sub_compact(self):
        self.assertEqual(calc.subtract(15,5),10)
        self.assertEqual(calc.subtract(192,2),190)
        self.assertEqual(calc.subtract(200,199),1)
        self.assertEqual(calc.subtract(135,5),130)
        self.assertEqual(calc.subtract(99,3),96)
        self.assertEqual(calc.subtract(15,2),13)
        
