#!/usr/bin/env python3
"""
Solves the min operations problem

functions:
  * minOperations(n): returns solution to min operations problem
"""


def minOperations(n):
    """
    finds mininum operations to reach n characters
    Argument:
      n: integer
    """
    chars = 2
    ops = 2
    cp = 2

    while chars != n:
        if n % chars != 0:
            chars += cp
            ops += 1
        else:
            cp = chars
            chars *= 2
            ops += 2
    return ops
