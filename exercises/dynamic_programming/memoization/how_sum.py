""""
Write a function how_sum(targetSum, numbers) that takes in a targetSum and an array of numbers as arguments. The
function should return an array containing any combination of elements that add up to exactly the targetSum. If there is
no combination that adds up to the targetSum, then return null. If there are multiple combinations possible, you may
return any single one.
"""


def how_sum(target_number: int, numbers: [], memo: {}) -> []:

    if memo.get(target_number):
        return memo[target_number]

    if target_number == 0:
        return []

    if target_number < 0:
        return None

    for number in numbers:
        current = target_number - number
        remainder_result = how_sum(current, numbers, memo)
        if remainder_result is not None:
            remainder_result.append(number)
            memo[target_number] = remainder_result
            return memo[target_number]

    memo[target_number] = None
    return None


if __name__ == "__main__":
    print(how_sum(7, [2, 3], {}))
    print(how_sum(7, [5, 3, 4, 7], {}))
    print(how_sum(7, [2, 4], {}))
    print(how_sum(8, [2, 3, 5], {}))
