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