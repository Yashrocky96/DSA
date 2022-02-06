"""
Merging 2 given sorted LL using recursion O(1) and O(N) space
because of recursion stack
"""
def mergeTwoLists(l1, l2):
    # Base condtiions
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    # Making the smaller node pointing to larger node
    if l1.val <= l2.val:
        temp = l1
        temp.next = mergeTwoLists(l1.next, l2)
    else:
        temp = l2
        temp.next = mergeTwoLists(l1, l2.next)
    return temp

"""
Iterative approach of merging two lists
"""
def mergeTwoLists(left, right):
    # Base conditions
    if left is None:
        return right
    if right is None:
        return left

    # Base check and initializing result pointer
    if left.val <= right.val:
        result = left
        left = left.next
    else:
        result = right
        right = right.next

    temp = result
    # traversing left and right and merging them
    while left and right:
        # Check left or right value and insert into result
        if left.val <= right.val:
            temp.next = left
            left = left.next
        else:
            temp.next = right
            right = right.next
        temp = temp.next

    # Whichever list is not empty join that to the result
    if left:
        temp.next = left
    if right:
        temp.next = right
        
    return result