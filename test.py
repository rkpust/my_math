from my_math import mm
import unittest

class TestMyMath(unittest.TestCase):
    # Constant
    def test_PI(self):
        self.assertEqual(mm.PI, 3.141592653589793)

    # Arithmetic
    def test_add(self):
        self.assertEqual(mm.add(5), 5)
        self.assertEqual(mm.add(-1, 1), 0)
        self.assertEqual(mm.add(1, 2, 4), 7)
        self.assertEqual(mm.add(1, 5, -4, 8), 10)


if __name__ == "__main__":
    unittest.main()
