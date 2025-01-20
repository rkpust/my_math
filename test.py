from my_math import mm
import unittest

class TestMyMath(unittest.TestCase):
    # Constant
    def test_PI(self):
        self.assertEqual(mm.PI, 3.141592653589793)


if __name__ == "__main__":
    unittest.main()
