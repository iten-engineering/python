import unittest
from calculator import add, sub, mul, div

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        expected = 6
        result = add(1,5)
        self.assertEqual(expected, result)
    
    def test_sub(self):
        expected = -4
        result = sub(1,5)
        self.assertEqual(expected, result)

    def test_mul(self):
        self.assertEqual( 12, mul(4,3))
        self.assertEqual( 12, mul(1,12))
        self.assertEqual( 12, mul(2,6))
        self.assertEqual( -3, mul(-1,3))

if __name__ == '__main__':
    unittest.main()
