import unittest
from MathUtil import MathUtil

class MathUtilTest(unittest.TestCase):

    # constructor if some fields are used.
    # For the current case, the constructor would not be needed)
    def __init__(self, *args, **kwargs):
       super(MathUtilTest, self).__init__(*args, **kwargs)

    def test_max(self):
        expected = 20
        actual = MathUtil.max(5,12,20)
        self.assertEqual(expected, actual)
        self.assertEqual(49, MathUtil.max(49,3,14))

    def test_min(self):
        self.assertEqual(5, MathUtil.min(5,12,20))
        self.assertEqual(3, MathUtil.min(49,3,14))

if __name__ == '__main__':
    unittest.main()
