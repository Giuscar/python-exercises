""""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:
1 <= n <= 45
"""


def climbing_stairs_solution_1(stairs_remaining, saved_results):
    if stairs_remaining == 0:
        return 1
    if stairs_remaining < 0:
        return 0
    if saved_results.get(stairs_remaining) and stairs_remaining == saved_results[stairs_remaining]:
        return saved_results[stairs_remaining]

    saved_results[stairs_remaining] = climbing_stairs_solution_1(stairs_remaining - 1, saved_results) +\
                                      climbing_stairs_solution_1(stairs_remaining - 2, saved_results)
    return saved_results[stairs_remaining]


def climbing_stairs_solution_2(stairs_remaining):
    if stairs_remaining == 1:
        return 1

    results = [0]*(stairs_remaining+1)
    results[1] = 1
    results[2] = 2

    for i in range(3, stairs_remaining+1):
        results[i] = results[i-1] + results[i-2]

    return results[stairs_remaining]


if __name__ == "__main__":
    print(climbing_stairs_solution_1(3, {}))
    print(climbing_stairs_solution_2(3))