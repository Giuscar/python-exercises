""""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return
the index where it would be if it were inserted in order.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0


Constraints:
- 1 <= nums.length <= 104
- 104 <= nums[i] <= 104
- nums contains distinct values sorted in ascending order.
- 104 <= target <= 104
"""


def binarySearch(nums, p, r, target):
    if p > r:
        return p

    if target < nums[p]:
        return p

    if target > nums[r]:
        return r + 1

    q = (p + r) // 2

    if nums[q] == target:
        return q
    elif nums[q] > target:
        return binarySearch(nums, p, q - 1, target)
    else:
        return binarySearch(nums, q + 1, r, target)


if __name__ == "__main__":
    target = 5
    nums = [1, 3, 5, 6]
    print(str(binarySearch(nums, 0, len(nums) - 1, target)))
