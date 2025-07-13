"""
Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two
directions, right and down, but certain cells are 'off limits' such that the robot cannot step on them. Design an
algorithm to find a path for the robot from the top left to the bottom right.
"""

from typing import List, Optional


class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def robot_in_grid(
    grid: List[List[int]],
    row: int = 0,
    col: int = 0,
    path: Optional[List[Position]] = None,
    visited: Optional[set] = None,
) -> Optional[List[Position]]:
    if path is None:
        path = []
    if visited is None:
        visited = set()

    rows = len(grid)
    cols = len(grid[0])

    # Check boundaries and off-limit cells
    if row >= rows or col >= cols or grid[row][col] == 1:
        return None

    pos = Position(row, col)

    # Avoid cycles (optional here since movement is only right/down, but safer)
    if (row, col) in visited:
        return None

    path.append(pos)
    visited.add((row, col))

    # Check if we've reached the bottom-right corner
    if row == rows - 1 and col == cols - 1:
        return path

    # Move right
    right_path = robot_in_grid(grid, row, col + 1, path.copy(), visited.copy())
    if right_path is not None:
        return right_path

    # Move down
    down_path = robot_in_grid(grid, row + 1, col, path.copy(), visited.copy())
    if down_path is not None:
        return down_path

    # No path found, backtrack
    return None


if __name__ == "__main__":
    rows = 5
    cols = 5
    # 0 = open cell, 1 = off limits
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ]

    path = robot_in_grid(grid)
    if path:
        print("Path found:")
        print(path)
    else:
        print("No path found.")
