""""
Say that you are a traveler on a 2D grid. You begin in the top-left corner and your goal is to travel to the bottom-right
corner. You may only move down or right. In how many ways you travel to the goal on a grid with dimnesions m*n? Write
a function 'grid_traveler(m, n)' that calculates this.
"""


def calculate_possible_solutions(m: int, n: int) -> int:
    grid_traveler = [[0 for i in range(n+1)] for j in range(m+1)]
    grid_traveler[1][1] = 1

    for i in range(m+1):
        for j in range(n+1):
            current = grid_traveler[i][j]
            if i+1 <= m:
                grid_traveler[i+1][j] += current

            if j+1 <= n:
                grid_traveler[i][j+1] += current

    return grid_traveler[m][n]


if __name__ == '__main__':
    print(calculate_possible_solutions(1, 1))
    print(calculate_possible_solutions(2, 3))
    print(calculate_possible_solutions(3, 2))
    print(calculate_possible_solutions(3, 3))
    print(calculate_possible_solutions(18, 18))