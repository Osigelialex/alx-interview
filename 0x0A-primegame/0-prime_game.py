#!/usr/bin/python3
"""Module for solving the prime game problem
"""


def is_prime(N):
    """verifies if a number is a prime number
    """
    if N < 2:
        return False
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Evaluates the winner of the game
    """
    def play(N):
        """Plays a current round of the game
        """
        maria_turn = True
        found_winner = False
        round_winner = False
        values = [x for x in range(N + 1)]

        while not found_winner:
            choice = -1
            for i in range(len(values)):
                if is_prime(values[i]):
                    choice = values[i]
                    break

            if choice == -1:
                found_winner = True
                round_winner = 'maria' if not maria_turn else 'ben'
                break

            values = list(filter(lambda x: x % choice != 0, values))
            maria_turn = False if maria_turn else True

        return round_winner

    m_points = 0
    b_points = 0
    for i in range(x):
        winner = play(nums[i])
        if winner == 'maria':
            m_points += 1
        else:
            b_points += 1

    return 'Maria' if m_points > b_points else 'Ben'
