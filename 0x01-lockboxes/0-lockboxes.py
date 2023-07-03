#!/usr/bin/python3
"""
Solves the locked box problem

functions
  * canUnlockAll(boxes): checks if all boxes can be unlocked
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked

    Arguments:
      boxes: a List of boxes each containing a List of keys

    Return:
      True if all boxes can be unlocked otherwise False
    """
    keys = set()

    for box in range(len(boxes)):
        for key in (boxes[box]):
            if key != box:
                keys.add(key)

    for idx in range(1, len(boxes)):
        if idx not in keys:
            return False

    return True
