""""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.



Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5


Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
import collections
from itertools import groupby
from typing import List


def repeatedNTimesSolution1(A: List[int]) -> int:
    N = len(A)//2
    return [int(k) for k, v in groupby(sorted(A))
            if len(list(v)) == N][0]


def repeatedNTimesSolution2(A: List[int]) -> int:
    count = collections.Counter(A)
    for k in count:
        if count[k] > 1:
            return k


if __name__ == "__main__":
    print(repeatedNTimesSolution1([1, 2, 3, 3]))
    print(repeatedNTimesSolution2([1, 2, 3, 3]))
