#!/usr/bin/python3
"""
Solves the min operations problem

functions:
  * minOperations(n): returns solution to min operations
"""


def minOperations(n) -> int:
    """
    finds mininum operations to reach n characters
    Argument:
      n: integer
    """
    if n <= 1:
        return 0

    characters = 2
    minimum_operations = 2
    copied = 1

    while characters != n:
        if n % characters != 0:
            characters += copied
            minimum_operations += 1
        else:
            copied = characters
            characters *= 2
            minimum_operations += 2

    return minimum_operations
