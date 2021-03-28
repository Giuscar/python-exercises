""""
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to
a specific target number.Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where
1 <= answer[0] < answer[1] <= numbers.length. You may assume that each input would have exactly one solution and you may
not use the same element twice.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]


Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in increasing order.
-1000 <= target <= 1000
Only one valid answer exists.
"""


def execute_two_sums_quadratic_solution(array, target):

    for i in range(0, len(array)):
        if i - 1 > 0 and array[i-1] == array[i]:
            continue
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i+1, j+j]

    return []


def execute_two_sums_linear_solution(array, target):
    l = 0
    r = len(array) - 1

    while l < r:
        s = array[l] + array[r]
        if s == target:
            return [l+1, r+1]
        elif s > target:
            r -= 1
        elif s < target:
            l += 1


if __name__ == "__main__":
    array = [2, 7, 11, 15]
    target = 9
    print(str(execute_two_sums_quadratic_solution(array, target)))
    print(str(execute_two_sums_linear_solution(array, target)))