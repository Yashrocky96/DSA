"""
Insertions in a linked list
at beginning or end using two pointers head and tail
Given only the class to solve the problem
Main is handled by the problem maker
"""

from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""

class Solution:
    def __init__(self):
        self.head = self.tail = None

    def insertAtEnd(self, data):
        new_node = ListNode.ListNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insertAtBeginning(self, data):
        new_node = ListNode.ListNode(data)

        if self.tail is None:
            self.tail = new_node

        new_node.next = self.head
        self.head = new_node
