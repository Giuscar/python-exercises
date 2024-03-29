""""
In the army each soldier has an assigned rank. A soldier of rank X has to report to (any) soldier of rank X + 1. Many
soldiers can report to the same superior. Write a function that, given an array A consisting of soldiers' ranks, returns
the number of soldiers who can report to some superior.

Examples:

    1) Give ranks=[3, 4, 3, 0, 2, 2, 3, 0, 0] your function should return because:
    - Three soldiers of rank 3 (ranks[0], ranks[2], ranks[6]) may report to a soldier of rank 4 (ranks[1]).
    - Two soldiers of rank 2 may report to any soldier of rank 3.

    2) Given ranks=[4,2,0] your function should return 0

    3) Given ranks=[4,4,3,3,1,0] your function should return 3, because:
    - A soldier of rank 0 can report to a soldier fo rank 1
    - Two soldiers of rank 3 can report to any soldier of rank 4

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [2..100000]
- Each element of array ranks is an integer within the range [0...1000000000]
"""


def number_of_soldiers_can_report(soldiers: []) -> int:
    filtered_soldiers = set(soldiers)
    return sum(1 for soldier in soldiers if soldier + 1 in filtered_soldiers)


if __name__ == "__main__":
    soldiers = [3, 4, 3, 0, 0, 2, 3, 0, 0]
    print(f"The number of soldiers reporting is {number_of_soldiers_can_report(soldiers)}")
