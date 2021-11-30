"""
This removes a node from the linked list
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
        self.head = None

    def linkedListRemove(self, x):
        temp = self.head
        if self.head is None:
            return None
        elif self.head.val == x:
            self.head = self.head.next
            return
        else:
            while temp.next is not None:
                if temp.next.val == x:
                    # Implements removal
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return self.head
