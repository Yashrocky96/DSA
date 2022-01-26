"""
Given two LL as numbers add them and return a LL
Similar problem as in arrays
"""
from Reversing_LL import reverseLinkedList

# Definition for ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add(n1, n2):
    # Base conditions
    if n1 is None:
        return n1
    if n2 is None:
        return n2
 
    # Reverse given numbers for addition
    n1 = reverseLinkedList(n1)
    n2 = reverseLinkedList(n2)
 
    # Storing head whose reverse is to be returned This is where will be final node
    head = n1
    prev = None
    c = 0
    sum = 0
     
    while n1 is not None and n2 is not None:
        sum = c + n1.val + n2.val
        n1.val = sum % 10
        c = int(sum / 10)
        prev = n1
        n1 = n1.next
        n2 = n2.next
         
    if n1 is not None or n2 is not None:
        if n2 is not None:
            prev.next = n2
        n1 = prev.next
         
        while n1 is not None:
            sum = c + n1.val
            n1.val = sum % 10
            c = int(sum / 10)
            prev = n1
            n1 = n1.next
             
    if c > 0:
        prev.next = ListNode(c)
         
    return reverseLinkedList(head)