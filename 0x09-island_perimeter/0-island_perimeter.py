#!/usr/bin/python3
"""
module for solving island perimeter problem
"""


def island_perimeter(grid):
    """finds perimeter of island in grid"""
    visited = set()

    def dfs(i, j):
        if grid[i][j] == 0:
            return 1

        if (i, j) in visited:
            return 0

        visited.add((i, j))
        perim = dfs(i - 1, j)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i, j + 1)
        return perim

    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == 1:
                return dfs(i, j)
