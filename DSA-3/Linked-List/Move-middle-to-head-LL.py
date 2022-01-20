"""
Moving from middle to starting using slow and fast pointers
"""

def move_middle_to_head(head):
    # Base Conditions
    if head is None or head.next is None:
        return head

    # Base variables
    prev, slow, fast = None, head, head

    while fast and fast.next:
        # store previous before moving to mid
        prev = slow
        # slow is the mid value when loop ends
        slow = slow.next
        # fast moves at 2x speed
        fast = fast.next.next

    # Last logic that removes mid from LL
    prev.next = slow.next
    # Joins it at start of LL
    slow.next = head
    head = slow

    return head