"""
Given a natural number, In how many ways can you make combinations of consecutive numbers such that sum is the number.
e. g. If N=15, then 1+2+3+4+5, 4+5+6, 7+8; output 3
"""


def get_combination_natural_numbers(N):
    L = 1
    count = 0

    while L*(L+1)/2 < N:
        a = (1.0 * N - (L * (L + 1) ) / 2) / (L + 1)
        if a - int(a) == 0.0:
            count += 1
        L += 1

    return count


if __name__ == "__main__":
    print(get_combination_natural_numbers(15))