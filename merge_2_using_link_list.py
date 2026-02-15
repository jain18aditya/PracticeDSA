"""
Problem: Merge Two Sorted Linked Lists

You are given the heads of two singly linked lists, both sorted in
non-decreasing order. Merge the two lists into one sorted linked list
and return the head of the merged list.

The merged list should be created by reusing the existing nodes
(splice together the nodes of the first two lists).

Requirements:
- The input linked lists are already sorted.
- The output linked list must also be sorted.
- Do not create new nodes for values; reuse existing nodes.
- Handle edge cases where one or both lists are empty.

Example:
Input:
List 1: 1 -> 3 -> 5 -> 7
List 2: 2 -> 4 -> 6 -> 8

Output:
Merged List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8

Approach:
Use an iterative method with a dummy node. Compare the current nodes
of both lists and attach the smaller node to the merged list, moving
forward until one list is exhausted. Then attach the remaining nodes
of the other list.
"""

# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Function to merge two sorted linked lists
def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    tail = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next

        tail = tail.next

    # Attach remaining nodes
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


# Helper function to create linked list from array
def createLinkedList(arr):
    head = None
    tail = None

    for val in arr:
        node = ListNode(val)
        if not head:
            head = node
        else:
            tail.next = node
        tail = node

    return head


# Helper function to print linked list
def printLinkedList(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()



list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

l1 = createLinkedList(list1)
l2 = createLinkedList(list2)

print("List 1:")
printLinkedList(l1)

print("List 2:")
printLinkedList(l2)

merged = mergeTwoLists(l1, l2)

print("Merged List:")
printLinkedList(merged)
