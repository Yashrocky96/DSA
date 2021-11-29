"""
Main I/O handled by problem maker
given function finds the element x that needs to be seached
in O(n) time.
"""

from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListSearch(head, x):
	if head is None:
		return False
	else:
		while True:
			if head.val == x:
				return True
			elif head.next is None:
				return False
			else:
				head = head.next
