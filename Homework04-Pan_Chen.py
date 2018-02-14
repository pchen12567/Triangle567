"""
Created on Feb 13 11:28:32 2018

@author: Pan Chen
"""
import unittest


def classify_triangle(a, b, c):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (ValueError, TypeError):
        return 'InvalidInput'

    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'

    a2 = round(a ** 2, 5)
    b2 = round(b ** 2, 5)
    c2 = round(c ** 2, 5)

    if (a + b) > c and (a + c) > b and (b + c) > a:
        if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
            if a == b or b == c or a == c:
                return 'Right Isosceles'
            else:
                return 'Right Scalene'
        elif a == b == c:
            return 'Equilateral'
        elif a == b or b == c or a == c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'


class TestTrianlges(unittest.TestCase):
    def test001(self):
        self.assertNotEqual(classify_triangle(1.1, 1.2, 1.3), 'InvalidInput')

    def test002(self):
        self.assertEqual(classify_triangle('x', 1, 1), 'InvalidInput')

    def test003(self):
        self.assertEqual(classify_triangle(None, 1, 1), 'InvalidInput')

    def test004(self):
        self.assertNotEqual(classify_triangle(198, 199, 200), 'InvalidInput')

    def test005(self):
        self.assertEqual(classify_triangle(-1, 1, 1), 'InvalidInput')

    def test006(self):
        self.assertEqual(classify_triangle(0, 1, 1), 'InvalidInput')

    def test007(self):
        self.assertEqual(classify_triangle(199, 200, 201), 'InvalidInput')

    def test008(self):
        self.assertNotEqual(classify_triangle(2, 3, 4), 'NotATriangle')

    def test009(self):
        self.assertNotEqual(classify_triangle(3, 4, 2), 'NotATriangle')

    def test010(self):
        self.assertNotEqual(classify_triangle(4, 2, 3), 'NotATriangle')

    def test011(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')

    def test012(self):
        self.assertEqual(classify_triangle(2, 3, 1), 'NotATriangle')

    def test013(self):
        self.assertEqual(classify_triangle(3, 1, 2), 'NotATriangle')

    def test014(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene')

    def test015(self):
        self.assertEqual(classify_triangle(4, 5, 3), 'Right Scalene')

    def test016(self):
        self.assertEqual(classify_triangle(5, 3, 4), 'Right Scalene')

    def test017(self):
        self.assertNotEqual(classify_triangle(2, 3, 4), 'Right Scalene')

    def test018(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral')

    def test019(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles')

    def test020(self):
        self.assertEqual(classify_triangle(2, 1, 2), 'Isosceles')

    def test021(self):
        self.assertEqual(classify_triangle(2, 2, 1), 'Isosceles')

    def test022(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')

    def test023(self):
        self.assertEqual(classify_triangle(3, 4, 2), 'Scalene')

    def test024(self):
        self.assertEqual(classify_triangle(4, 2, 3), 'Scalene')

    def test025(self):
        self.assertEqual(classify_triangle(1, 1, 2 ** 0.5), 'Right Isosceles')

    def test026(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene')
        print('3,4,5 is a Right Scalene Triangle')

    def test027(self):
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')
        print('3,3,3 is an Equilateral Triangle')

    def test028(self):
        self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles')
        print('1,2,2 is an Isosceles Triangle')

    def test029(self):
        self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
        print('2,3,4 is a Scalene Triangle')

    def test030(self):
        self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')
        print('1,2,3 is not a Triangle')


if __name__ == '__main__':
    unittest.main(exit=False)
