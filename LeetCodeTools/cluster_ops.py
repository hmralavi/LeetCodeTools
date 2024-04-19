from typing import List


def numIslands(grid: List[List[str]]) -> int:
    """
    Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.

    An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    Args:
        grid (List[List[str]]): m x n 2D binary grid.
    """

    rows = len(grid)
    cols = len(grid[0])

    def propagate(r, c):
        if r >= rows or r < 0 or c >= cols or c < 0 or grid[r][c] != "1":
            return
        grid[r][c] = "0"
        propagate(r - 1, c)
        propagate(r + 1, c)
        propagate(r, c - 1)
        propagate(r, c + 1)

    n = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                n += 1
                propagate(r, c)

    return n
