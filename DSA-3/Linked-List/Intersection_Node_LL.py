"""
Given two linked lists this program finds the intersection
"""

# Counts the number of nodes in a LL
def len_LL(head):
    # Base variables
    temp, length = head, 0
    while temp:
        length += 1
        temp = temp.next
    return length

# Pass head and number of nodes to move up to match with smaller LL
def move_large_LL(head, n):
    temp = head
    for i in range(n):
        temp = temp.next
    return temp

def get_intersection_node(lst1, lst2):
    len1 = len_LL(lst1)
    len2 = len_LL(lst2)
    
    # Compare lengths of LL
    diff = abs(len1 - len2)
    if len1 > len2:
        temp1 = move_large_LL(lst1, diff)
        temp2 = lst2
    else:
        temp1 = lst1
        temp2 = move_large_LL(lst2, diff)
    
    # Loop to None if match found then there's intersection
    while temp1:
        if temp1.val == temp2.val:
            return temp1

        temp1 = temp1.next
        temp2 = temp2.next

    return None