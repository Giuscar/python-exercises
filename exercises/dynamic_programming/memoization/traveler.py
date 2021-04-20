""""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right. In how many ways you travel to the goal on a grid with dimnesions m*n? Write
a function 'grid_traveler(m, n)' that calculates this.
"""


def grid_traveler(x: int, y: int, memo: dict) -> []:
    index = str(x) + ',' + str(y)

    if memo.get(index):
        return memo[index]

    if x == 1 and y == 1:
        return 1

    if x == 0 or y == 0:
        return 0

    memo[index] = grid_traveler(x-1, y, memo) + \
                  grid_traveler(x, y-1, memo)

    return memo[index]


if __name__ == '__main__':
    print(grid_traveler(1, 1, dict()))
    print(grid_traveler(2, 3, dict()))
    print(grid_traveler(3, 2, dict()))
    print(grid_traveler(3, 3, dict()))
    print(grid_traveler(18, 18, dict()))