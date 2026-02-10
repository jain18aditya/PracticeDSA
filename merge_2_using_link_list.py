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
