"""
Using this function remove duplicates in a LL using hashing
"""

def remove_duplicates(head):
    # Base conditions and inits
    if head is None or head.next is None:
        return head
    temp = head

    # Set to check if already exists or not
    mp = set()
    mp.add(head.val)

    while temp.next is not None:
        if temp.next.val in mp:
            temp.next = temp.next.next
        else:
            mp.add(temp.next.val)
            temp = temp.next
    return head