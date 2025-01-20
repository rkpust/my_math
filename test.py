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

    def test_sub(self):
        self.assertEqual(mm.sub(5, 2), 3)
        self.assertEqual(mm.sub(-5, -2), -3)
        self.assertEqual(mm.sub(-5, 2), -7)
        self.assertEqual(mm.sub(5, -2), 7)

    def test_mul(self):
        self.assertEqual(mm.mul(3), 3)
        self.assertEqual(mm.mul(-1, 4), -4)
        self.assertEqual(mm.mul(5, 2, 4), 40)
        self.assertEqual(mm.mul(1, 5, 0, 8), 0)

    def test_div(self):
        self.assertEqual(mm.div(10, 2), 5.0)
        self.assertEqual(mm.div(15, -3), -5.0)
        self.assertEqual(mm.div(-20, 5), -4.0)
        self.assertEqual(mm.div(5, 2), 2.5)
        self.assertEqual(mm.div(20, 3), 6.666666666666667)
        self.assertEqual(mm.div(2.5, 4), 0.625)
        self.assertEqual(mm.div(25, 4.5), 5.555555555555555)
        self.assertEqual(mm.div(0, 3), 0.0)
        self.assertEqual(mm.div(0, -4), -0.0)
        self.assertEqual(mm.div(2, 0), 'ZeroDivisionError: division by zero')

    def test_mod(self):
        self.assertEqual(mm.mod(10, 2), 0)
        self.assertEqual(mm.mod(15, -3), 0)
        self.assertEqual(mm.mod(-20, 3), 1)
        self.assertEqual(mm.mod(20, 3), 2)
        self.assertEqual(mm.mod(5, 2.3), 0.40000000000000036)
        self.assertEqual(mm.mod(25, 4.5), 2.5)
        self.assertEqual(mm.mod(0, -3), 0)
        self.assertEqual(mm.mod(2, 0), 'ZeroDivisionError: integer division or modulo by zero')

    def test_flr_div(self):
            self.assertEqual(mm.flr_div(10, 2), 5)
            self.assertEqual(mm.flr_div(15, -3), -5)
            self.assertEqual(mm.flr_div(-20, 5), -4)
            self.assertEqual(mm.flr_div(5, 2), 2)
            self.assertEqual(mm.flr_div(20, 3), 6)
            self.assertEqual(mm.flr_div(2.5, 4), 0.0)
            self.assertEqual(mm.flr_div(25, 4.5), 5.0)
            self.assertEqual(mm.flr_div(0, 3), 0)
            self.assertEqual(mm.flr_div(0, -4), 0)
            self.assertEqual(mm.flr_div(2, 0), 'ZeroDivisionError: integer division or modulo by zero')

        
if __name__ == "__main__":
    unittest.main()
