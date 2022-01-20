class Node:
	def __init__(self, _val, _next, _random):
		self.val = _val
		self.next = _next
		self.random = _random

def copyListWithRandomPointer(head):
	# Base conditions
	if head is None:
		return None
	elif head.next is None:
		newNode = Node(head.val, None, None)
		return newNode
	
	# Loop list and insert new list nodes in between
	temp = head
	while temp:
		new = Node(temp.val, temp.next, None)
		temp.next = new
		temp = temp.next.next

	# loop again and set the new node random references properly
	temp = head
	while temp:
		if temp.random != None:
			temp.next.random = temp.random.next
		temp = temp.next.next
	
	# Segregate the two lists and return duplicate head to return the Deep copy
	temp = head
	dup_root = head.next
	while temp.next:
		buff = temp.next
		temp.next = temp.next.next
		temp = buff
	return dup_root