# -*- coding: utf-8 -*-
"""
Created on  Feb 27 13:44:00 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Pan Chen
"""


def classify_triangle(side_a, side_b, side_c):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right Scalene'
        If the sum of any two sides equals the squate of the third side
        and exactly one pair of sides are equal,then return 'Right Isosceles'
    """
    # verify that all 3 inputs are integers or floats
    # require that the input values be > 0 and <= 200
    try:
        side_a = float(side_a)
        side_b = float(side_b)
        side_c = float(side_c)
    except (ValueError, TypeError):
        return 'InvalidInput'

    if any([side_a > 200, side_b > 200, side_c > 200]) \
            or any([side_a <= 0, side_b <= 0, side_c <= 0]):
        return 'InvalidInput'

    side_a2 = round(side_a ** 2, 5)
    side_b2 = round(side_b ** 2, 5)
    side_c2 = round(side_c ** 2, 5)

    if (side_a + side_b) > side_c and (side_a + side_c) > side_b and (side_b + side_c) > side_a:
        if side_a2 + side_b2 == side_c2 \
                or side_a2 + side_c2 == side_b2 \
                or side_b2 + side_c2 == side_a2:
            if side_a == side_b or side_b == side_c or side_a == side_c:
                return 'Right Isosceles'
            else:
                return 'Right Scalene'
        elif side_a == side_b == side_c:
            return 'Equilateral'
        elif side_a == side_b or side_b == side_c or side_a == side_c:
            return 'Isosceles'
        else:
            return 'Scalene'
    else:
        return 'NotATriangle'
