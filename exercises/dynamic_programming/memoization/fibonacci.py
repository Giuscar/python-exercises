""""
Calculate fibonacci series at n-th input position.
"""


def calculate_fibonacci_series(n: int, memo: dict) -> int:
    if memo.get(n):
        return memo[n]
    if n < 0:
        my_error = ValueError(str(n) + ' should be a positive number')
        raise my_error
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = calculate_fibonacci_series(n-1, memo) + calculate_fibonacci_series(n-2, memo)
    return memo[n]


if __name__ == '__main__':
    n = 10
    memo = {}
    try:
        print(calculate_fibonacci_series(n, memo))
    except AssertionError:
       print('Numbers is negative')