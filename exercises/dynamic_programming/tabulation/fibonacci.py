""""
Calculate fibonacci series at n-th input position.
"""
import numpy as np


def calculate_fibonacci_series(n: int) -> int:
    if n < 0:
        raise ValueError(str(n) + ' ' + 'should be a positive value')

    if n == 0:
        return 0

    tab = np.zeros(n+1)
    tab[1] = int(1)

    for val in range(2, len(tab)):
        tab[val] = int(tab[val-1]) + int(tab[val-2])
    return int(tab[len(tab)-1])


if __name__ == '__main__':
    n = 200
    try:
        print(calculate_fibonacci_series(n))
    except AssertionError:
        print('Negative value')
