"""
given node find the node and delete it from the linked list
"""

def delete_middle_node(head, node):
    if head is None or node == head:
        return None
    
    temp = head
    while temp:
        prev = temp
        temp = temp.next
        if temp == node:
            prev.next = temp.next

    return head