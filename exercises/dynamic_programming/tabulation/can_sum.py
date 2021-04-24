""""
Write a function can_sum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The
function should return a boolean indicating whether or not it is possible to generate the targetSum using numbers from
the array. You may use element the array as many times as needed. You may assume that all input numbers are nonnegative.
"""


def can_sum(target_number: int, numbers: []) -> bool:
    array_values = [False]*(target_number+1)
    array_values[0] = True

    for idx in range(target_number):
        if array_values[idx] is True:
            for number in numbers:
                if idx+number < len(array_values):
                    array_values[idx+number] = True
                    if idx + number == target_number:
                        return True

    return False


if __name__ == '__main__':
    print(can_sum(7, [2, 3]))
    print(can_sum(7, [5, 3, 4, 7]))
    print(can_sum(7, [2, 4]))
    print(can_sum(8, [2, 3, 5]))
    print(can_sum(300, [7, 4]))