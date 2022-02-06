"""
RECURSIVE ----- Sorting list in NlogN time using Merge Sort on LL
"""
def get_Middle(head):
    ''' Finds middle node of a LL'''
    # Base Conditions
    if head == None:
        return head

    # Base variables
    slow, fast = head, head

    while fast.next and fast.next.next:
        # slow is the mid value when loop ends
        slow = slow.next
        # fast moves at 2x speed
        fast = fast.next.next
    return slow

"""
Iterative approach of merging two lists - Efficiency increased by a high margin
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

def sort_list(head):
    # Base cases
    if head is None or head.next is None:
        return head

    # find the middle and middle's next and separate list into two
    mid = get_Middle(head)
    mid_next = mid.next

    mid.next = None

    # Recur on left and right lists and then perform merge sort on them
    left = sort_list(head)
    right = sort_list(mid_next)

    # Merge sort two lists and returns the head of the LL
    result = mergeTwoLists(left, right)

    return result