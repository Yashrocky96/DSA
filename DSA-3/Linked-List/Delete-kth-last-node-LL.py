"""
Given kth value delete a node that's kth node from the last Node
"""

def delete_kth_to_last(head, k):
    # Base condition, Since k is always valid
    if head is None or head.next is None:
        return None

    # Base variables or pointers
    temp, prev, ref = head, None, head

    # ref start at k nodes from head
    for i in range(k):
        ref = ref.next
    # Case when kth node becomes none and refers head
    if ref is None:
        head = head.next
        return head

    # Else handle all other cases, this loop finds the kth node
    while ref:
        prev = temp
        temp = temp.next

        ref = ref.next
    
    # End conition that deletes kth node
    prev.next = temp.next
    return head