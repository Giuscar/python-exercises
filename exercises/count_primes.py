""""
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
"""

from math import sqrt


def count_primes_solution_1(n: int) -> int:
    if n == 2:
        return 0

    if n == 3:
        return 1

    numbers = [i for i in range(n + 1)]
    count = 0

    for idx in range(2, len(numbers)):
        if numbers[idx] != -1:
            index = numbers[idx]
            while index + numbers[idx] < len(numbers):
                numbers[index + numbers[idx]] = -1
                index += numbers[idx]

    for idx in range(2, len(numbers)):
        if numbers[idx] != -1 and idx != n:
            count += 1

    return count


def count_primes_solution_2(n: int) -> int:
    if n < 2:
        return 0
    res = [1] * n
    res[0] = 0
    res[1] = 0
    for i in range(2, int(sqrt(n)) + 1):
        if res[i] == 1:
            for j in range(i + i, n, i):
                res[j] = 0
    return sum(res)


if __name__ == "__main__":
    print(count_primes_solution_1(4999))
    print(count_primes_solution_2(4999))
