from typing import List
""""
Given an array A of integers, return the number of (contiguous, non-empty) subarrays that have a sum divisible by K.

Example 1:
Input: A = [4,5,0,-2,-3,1], K = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by K = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Note:
1. 1 <= A.length <= 30000
2. -10000 <= A[i] <= 10000
3. 2 <= K <= 10000
"""


def subarraysDivByK(A: List[int], K: int) -> int:
    total = 0
    counts = [0]*K

    for val in A:
        total += val % K
        counts[total % K] += 1

    num_sub_arrays_div_by_k = counts[0]

    for count in counts:
        num_sub_arrays_div_by_k += (count*(count-1))//2

    return num_sub_arrays_div_by_k


if __name__ == "__main__":
    A = [4, 5, 0, -2, -3, 1]
    K = 5
    print("The number of subarray divisible by {0} is {1}".format(str(K), str(subarraysDivByK(A, K))))