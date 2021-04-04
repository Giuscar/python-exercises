""""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10

"""
from typing import List


def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    def backtrack(first=0, curr=[]):
        curr = sorted(curr)
        if len(curr) == i:

            for arr in output:
                if arr == curr:
                    return

            output.append(curr[:])
            return

        for idx in range(first, n):
            curr.append(nums[idx])
            backtrack(idx + 1, curr)
            curr.pop()

    output = [[]]
    n = len(nums)

    for i in range(n + 1):
        backtrack()

    return output


if __name__ == "__main__":
    print(subsetsWithDup([1, 2, 2]))