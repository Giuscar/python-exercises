""""
Write a function can_sum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The
function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from
the array. You may use element the array as many times as needed. You may assume that all input numbers are nonnegative.
"""


def can_sum(target_number: int, numbers: [], memo: {}) -> bool:

    if memo.get(target_number):
        return memo[target_number]
    elif target_number == 0:
        return True
    elif target_number < 0:
        return False

    for number in numbers:
        current = target_number - number
        if current >= 0 and can_sum(current, numbers, memo) is True:
            memo[target_number] = True
            return True

    memo[target_number] = False
    return False


if __name__ == '__main__':
    print(can_sum(7, [2, 3], {}))
    print(can_sum(7, [5, 3, 4, 7], {}))
    print(can_sum(7, [2, 4], {}))
    print(can_sum(8, [2, 3, 5], {}))