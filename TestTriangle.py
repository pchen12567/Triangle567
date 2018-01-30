# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle


# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testEquilateral1(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 is an Equilateral triangle')

    def testEquilateral2(self):
        self.assertNotEqual(classifyTriangle(1, 2, 2), 'Equilateral', '1,2,2 is not an Equilateral triangle')

    def testIsosceles1(self):
        self.assertEqual(classifyTriangle(1, 2, 2), 'Isosceles', '1,2,2 is an Isosceles triangle')

    def testIsosceles2(self):
        self.assertEqual(classifyTriangle(2, 1, 2), 'Isosceles', '2,1,2 is an Isosceles triangle')

    def testIsosceles3(self):
        self.assertEqual(classifyTriangle(2, 2, 1), 'Isosceles', '2,2,1 is an Isosceles triangle')

    def testIsosceles4(self):
        self.assertNotEqual(classifyTriangle(2, 3, 4), 'Isosceles', '2,3,4 is not an Isosceles triangle')

    def testRightTriangle1(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangle2(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testRightTriangle3(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangle4(self):
        self.assertNotEqual(classifyTriangle(2, 3, 4), 'Right', '2,3,4 is not a Right triangle')

    def testScalene1(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 is a Scalene triangle')

    def testScalene2(self):
        self.assertEqual(classifyTriangle(3, 4, 2), 'Scalene', '3,4,2 is a Scalene triangle')

    def testScalene3(self):
        self.assertEqual(classifyTriangle(4, 2, 3), 'Scalene', '4,2,3 is a Scalene triangle')

    def testScalene4(self):
        self.assertNotEqual(classifyTriangle(1, 2, 2), 'Scalene', '1,2,2 is not a Scalene triangle')

    def testNotATriangle1(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', '1,2,3 is not a triangle')

    def testNotATriangle2(self):
        self.assertEqual(classifyTriangle(2, 3, 1), 'NotATriangle', '2,3,1 is not a triangle')

    def testNotATriangle3(self):
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle', '3,1,2 is not a triangle')

    def testNotATriangle4(self):
        self.assertNotEqual(classifyTriangle(2, 3, 4), 'NotATriangle', '2,3,4 is a triangle')

    def testInvalidInput1(self):
        self.assertEqual(classifyTriangle(250, 1, 1), 'InvalidInput', '250,1,1 is InvalidInput')

    def testInvalidInput2(self):
        self.assertEqual(classifyTriangle(1, 250, 1), 'InvalidInput', '1,250,1 is InvalidInput')

    def testInvalidInput3(self):
        self.assertEqual(classifyTriangle(1, 1, 250), 'InvalidInput', '1,1,250 is InvalidInput')

    def testInvalidInput4(self):
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1,1,1 is InvalidInput')

    def testInvalidInput5(self):
        self.assertEqual(classifyTriangle(1, -1, 1), 'InvalidInput', '1,-1,1 is InvalidInput')

    def testInvalidInput6(self):
        self.assertEqual(classifyTriangle(1, 1, -1), 'InvalidInput', '1,1,-1 is InvalidInput')

    def testInvalidInput7(self):
        self.assertEqual(classifyTriangle(1.1, 1, 1), 'InvalidInput', '1.1,1,1 is InvalidInput')

    def testInvalidInput8(self):
        self.assertEqual(classifyTriangle(1, 1.1, 1), 'InvalidInput', '1,1.1,1 is InvalidInput')

    def testInvalidInput9(self):
        self.assertEqual(classifyTriangle(1, 1, 1.1), 'InvalidInput', '1,1,1.1 is InvalidInput')

    def testInvalidInput10(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput', '0,1,1 is InvalidInput')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
