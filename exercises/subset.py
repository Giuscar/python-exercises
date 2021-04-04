""""
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


def recursive_sub_set_solution_1(nums):
    outputs = [[]]
    for num in nums:
        outputs += [curr + [num] for curr in outputs]

    return outputs
    #[print(' '.join(list(map(str, output)))) for output in outputs]


def recursive_sub_set_solution_2(nums):
    def backtrack(first=0, occurr=[]):
        if len(occurr) == k:
            output.append(occurr[:])
            return

        for i in range(first, n):
            occurr.append(nums[i])
            backtrack(i + 1, occurr)
            occurr.pop()

    output = []
    n = len(nums)

    for k in range(n + 1):
        backtrack()

    return output


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(recursive_sub_set_solution_1(nums))
    print(recursive_sub_set_solution_2(nums))

