"""
Segregates even odd elements in separate lists
"""

from crio.ds.List import ListNode

"""
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

Use ListNode.ListNode(data) to create new node
"""


def linkedListSplit(head):
	# base case
	if head is None:
		return head, head
	else:
        # initialized needed pointers
		odd = odd_tail = even = even_tail = None
		while head is not None:
			check = head.val % 2
            # Check if val is even or odd
			if check == 1:
				# Perform odd ops
				if odd is None:
					odd = odd_tail = head
				else:
                    # appends to the previous item in list
					odd_tail.next = head
					odd_tail = head
			else:
				# Perform even ops
				if even is None:
					even = even_tail = head
				else:
					even_tail.next = head
					even_tail = head
            # Moves head to next item
            head = head.next

        # Handles edge cases and closes lists
		if odd_tail is not None:
			odd_tail.next = None
		if even_tail is not None:
			even_tail.next = None
	return odd, even
