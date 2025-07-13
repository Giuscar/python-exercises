"""
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time. Implement a
method to count how many possible ways the climb can run up the stairs
"""


def triple_step(n: int):
    """
    Calculates how many possible ways a person can run up the stairs.
    @:param n: number of total steps in a stairs
    """
    if n < 0:
        return 0
    elif n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        dp[i] += dp[i - 1] if i - 1 >= 0 else 0
        dp[i] += dp[i - 2] if i - 2 >= 0 else 0
        dp[i] += dp[i - 3] if i - 3 >= 0 else 0

    return dp[n]


if __name__ == "__main__":
    for i in range(10):
        print(f"Number of ways to climb a staircase with {i} steps: {triple_step(i)}")
