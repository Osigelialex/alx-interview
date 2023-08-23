#!/usr/bin/python3
"""Module for solving the making change problem
"""


def makeChange(coins, total) -> int:
    """
    Finds the least number of coins needed
    to arrive at total
    """
    coins.sort()
    total_coins = 0
    target = total

    for i in range(len(coins) - 1, 0, -1):
        if coins[i] <= target:
            total_coins += target // coins[i]
            target = target % coins[i]

    return -1 if target != 0 else total_coins
