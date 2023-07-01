#!/usr/bin/python3
"""
This script generates pascals triangle

functions:
  * pascal_triangle: returns pascals triangle to nth degree
"""


def pascal_triangle(n):
    """
    Generates pascals triangle to nth degree
    Arguments:
      n: an integer
    Return:
      generated pascal triangle
    """
    if n <= 0:
        return []

    triangle = []
    current_row = []

    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == 1 or j == i:
                current_row.append(1)
            else:
                prev_row = triangle[-1]
                current_row.append(prev_row[j - 1] + prev_row[j - 2])
        triangle.append(current_row)
        current_row = []

    return triangle
