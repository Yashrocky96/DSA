"""
Given circular sorted LL, find place, create node and insert into LL
"""
# Definition for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def insertIntoSortedCircularList(head, insertVal):
    new = ListNode(insertVal)
    # Base condition
    if head is None:
        new.next = new
        return new

    temp = head
    while True:
        prev = temp
        temp = temp.next

        # Main condition for most cases to insert between
        if insertVal >= prev.val and insertVal <= temp.val:
                prev.next = new
                new.next = temp
                return head
        # Handling min and max insertVal in List
        if prev.val > temp.val:
            if insertVal >= prev.val or insertVal <= temp.val:
                prev.next = new
                new.next = temp
                return head
        # Loop condition
        if temp == head:
            break

    # handles end conditions
    new.next = head
    prev.next = new
    return head