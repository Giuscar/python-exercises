""""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000


Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
which is more subtle.
"""


def maxSubArray(nums):
    total_sum = float("-inf")
    max_sum = float("-inf")

    for num in nums:
        total_sum = max(num, total_sum + num)
        max_sum = max(max_sum, total_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(str(maxSubArray(nums)))
