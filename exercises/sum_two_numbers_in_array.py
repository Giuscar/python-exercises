""""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.


Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Input: nums = [2,11,15,7]
Output: [0,3]
"""


def execute_solution(target: int, nums: []):
    if not nums:
        print('The input is invalid')
    else:
        dict_nums = {}
        for idx, value in enumerate(nums):
            dict_nums[value] = idx

        for idx in range(len(nums)):
            if dict_nums.get(target - nums[idx]):
                return idx, dict_nums[target - nums[idx]]


if __name__ == '__main__':
    n = 9
    nums = [2, 7, 11, 15]
    x, y = execute_solution(n, nums)

    print('The idx having sum {0} are ({1}, {2})'.format(str(n), str(x), str(y)))
