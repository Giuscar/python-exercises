""""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every
element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


def contains_duplicates_solution_1(nums: List[int]) -> bool:
    s = sorted(nums)
    index = 0

    while len(s) > 1:
        if s[index] == s[index+1]:
            return True
        s.pop(0)

    return False


def contains_duplicates_solution_2(nums: List[int]) -> bool:
    s = set()

    for i in range(0, len(nums)):
        if nums[i] in s:
            return True
        s.add(nums[i])

    return False


def contains_duplicates_solution_3(nums: List[int]) -> bool:
    s = sorted(nums)

    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            return True

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 5, 10, 4, 10]
    print(contains_duplicates_solution_1(nums))
    print(contains_duplicates_solution_2(nums))
    print(contains_duplicates_solution_3(nums))
