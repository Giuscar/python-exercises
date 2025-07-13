"""
A magic index in an array A[0..n-1] is defined to be an index such that A[i]=i. Given a sorted array of distinct
integers, write a method to find a magic index, if one exists, in array A.
"""

from typing import List


def magic_index(x: int, y: int, A: List):

    mid = (x + y) // 2
    if x > y:
        return None

    if A[mid] == mid:
        return mid
    if A[mid] > mid:
        return magic_index(x, mid - 1, A)
    else:
        return magic_index(mid + 1, y, A)


if __name__ == "__main__":

    A = [-10, -5, 0, 3, 7]
    result = magic_index(0, len(A), A)
    if result:
        print(f"The array is magic: A[{result}]={result}")
    else:
        print(f"The array is not magic")
