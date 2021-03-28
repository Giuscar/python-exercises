""""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:

Input: head = [1,1,2]
Output: [1,2]
Example 2:

Input: head = [1,1,2,3,3]
Output: [1,2,3]

Constraints:
The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fill_sorted_list():
    head = tail = ListNode(0)
    nodes = [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

    for node in nodes:
        tail.next = ListNode(node)
        tail = tail.next

    return head.next


def delete_duplicates_from_sorted_list(list_node):
    current = list_node

    while current != None and current.next != None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return list_node


def print_list(list_node):
    current = list_node

    while current != None:
        print(current.val)
        current = current.next


if __name__ == "__main__":
    list_node = fill_sorted_list()
    list_node = delete_duplicates_from_sorted_list(list_node)
    print_list(list_node)