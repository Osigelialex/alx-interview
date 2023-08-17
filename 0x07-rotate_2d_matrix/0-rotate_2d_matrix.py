#!/usr/bin/env python3
"""module for rotating a matrix clockwise
"""


def rotate_2d_matrix(matrix):
    """rotates matrix clockwise
    """
    left, right = 0, len(matrix) - 1
    up, down = left, right

    while left < right:
        for i in range(right - left):
            temp = matrix[up][left + i]
            matrix[up][left + i] = matrix[down - i][left]
            matrix[down - i][left] = matrix[down][right - i]
            matrix[down][right - i] = matrix[up + i][right]
            matrix[up + i][right] = temp

        up = left = left + 1
        down = right = right - 1
