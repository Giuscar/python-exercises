from itertools import accumulate

""""
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.

Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 
Constraints:
- 1 <= nums.length <= 2 * 104
- 1000 <= nums[i] <= 1000
- 107 <= k <= 107

"""


def subarraySum(nums, k):
    sum_freq = {0: 1}
    count = 0

    for num in accumulate(nums):
        count += sum_freq.get(num - k, 0)
        sum_freq[count] = sum_freq.get(num, 0) + 1

    return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print("The number of subarrays having sum equal to {0} is {1}".format(str(k), str(subarraySum(nums, k))))
