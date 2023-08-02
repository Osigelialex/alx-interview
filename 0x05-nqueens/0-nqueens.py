#!/usr/bin/python3
"""N Queens solver module"""
import sys


def is_safe(board, row, col, N):
    """Checks if cell is safe for queen"""
    for i in range(row):
        if board[i][col] == 1:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)] == 1:
            return False

        if col + (row - i) < N and board[i][col + (row - i)] == 1:
            return False

    return True


def nqueens_util(board, row, N, solutions):
    """insert queens at safe positions on board"""
    if row == N:
        solutions.append([[(i, j) for j in range(N) 
                           if board[i][j] == 1][0] for i in range(N)])
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def nqueens(N):
    """main function for nqueens solver"""
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    nqueens_util(board, 0, N, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solutions = nqueens(sys.argv[1])
    for solution in solutions:
        print(solution)
