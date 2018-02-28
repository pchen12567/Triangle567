# -*- coding: utf-8 -*-
"""
Created on  Feb 27 17:50:00 2018

The primary goal of this file is to demonstrate a simple unittest implementation

@author: Pan Chen
"""

import unittest

from Triangle import classify_triangle


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
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
        self.assertEqual(classify_triangle(199, 199, 201), 'InvalidInput')

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

    # def test026(self):
    #     self.assertEqual(classify_triangle(3, 4, 5), 'Right Scalene')
    #     print('3,4,5 is a Right Scalene Triangle')
    #
    # def test027(self):
    #     self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral')
    #     print('3,3,3 is an Equilateral Triangle')
    #
    # def test028(self):
    #     self.assertEqual(classify_triangle(1, 2, 2), 'Isosceles')
    #     print('1,2,2 is an Isosceles Triangle')
    #
    # def test029(self):
    #     self.assertEqual(classify_triangle(2, 3, 4), 'Scalene')
    #     print('2,3,4 is a Scalene Triangle')
    #
    # def test030(self):
    #     self.assertEqual(classify_triangle(1, 2, 3), 'NotATriangle')
    #     print('1,2,3 is not a Triangle')

    def test031(self):
        self.assertEqual(classify_triangle('hello', 1, 1), 'InvalidInput')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
