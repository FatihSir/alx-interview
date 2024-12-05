#!/usr/bin/python3
"""Island Perimeter Module"""


def island_perimeter(grid):
    """
    A function that calculates the perimeter of the island in the grid

    :param grid: rectangular of integer where
                 0 represents water and 1 represents land
    :return: perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0])
    total_perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                total_perimeter += 4
                if row > 0 and grid[row - 1][col] == 1:
                    total_perimeter -= 2
                if col > 0 and grid[row][col - 1] == 1:
                    total_perimeter -= 2
    return total_perimeter
