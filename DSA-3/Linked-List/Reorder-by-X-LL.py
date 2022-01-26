"""
Reordering the linked list using two pointers to segregate based on values
and comparing with given integer and then merging to get the result LL
"""
# This function takes a node and attaches to their heads and generates tail
def separate(temp, head, tail):
    if head is None:
        head = temp
        head.next = None
        tail = head
    else:
        tail.next = temp
        temp.next = None
        tail = tail.next
    return [head, tail]


def partition(head, x):
    h1, h2, h3 = None, None, None
    tail1, tail2, tail3 = None, None, None
    # Partition and store in different heads accordingly
    
    while head:
        # Storing curr node in temp
        temp = head
        head = head.next

        # h1 stores lesser values
        if temp.val < x:
            [h1, tail1] = separate(temp, h1, tail1)

        # h3 stores greater values
        elif temp.val > x:
            [h3, tail3] = separate(temp, h3, tail3)
        # h2 stores equal values
        else:
            [h2, tail2] = separate(temp, h2, tail2)
    
    # End condition of merging all heads
    # Pretty self-explanatory condition
    
    if h1 is None:
        if h2 is None:
            return h3
        tail2.next = h3
        return h2
    if h2 is None:
        tail1.next = h3
        return h1
    tail1.next = h2
    tail2.next = h3
            
    return h1