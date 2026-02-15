"""
Problem Statement:

Design and implement a singly linked list.

1. Create a ListNode class with value and next pointer.
2. Write a function to create a linked list from a given array of integers.
3. Write a function to traverse and print the linked list.

Example:
Input:  nums = [1, 2, 3, 4, 5]
Output: 1 -> 2 -> 3 -> 4 -> 5
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_link_list(nums):
    head = None
    tail = None
    for i in nums:
        node = ListNode(i)
        if not head:
            head = node
        else:
            tail.next = node
        tail = node
    return head


def print_link_list(head):
    while head:
        print(head.val, end=' ')
        head = head.next


nums = [1, 2, 3, 4, 5]
head = create_link_list(nums)
print_link_list(head)
