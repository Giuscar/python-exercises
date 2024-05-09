""""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false

Constraints:
1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""

from typing import List


def contains_duplicates(nums: List[int], k: int) -> bool:
    s = {}

    for i in range(0, len(nums)):
        if nums[i] in s and abs(i - s[nums[i]]) <= k:
            return True
        s[nums[i]] = i

    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(contains_duplicates(nums, 3))
