'''
# Definition for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
# Implement Solution Here
def reverseLinkedList(head):
    # Base condition
    if head is None or head.next is None:
        return head
    # Base inits
    prev, curr = None, head

    while head.next:
        # Store next to not miss the LL
        head = head.next
        # Current points to prev value initially None
        curr.next = prev
        # Move prev to current nodes
        prev = curr
        # move curr to head
        curr = head
    # Final node to point to the prev that'll store alll previous values
    head.next = prev

    return head