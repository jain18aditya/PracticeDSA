class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next      # save next
        curr.next = prev     # reverse link
        prev = curr          # move prev
        curr = nxt           # move curr

    return prev
