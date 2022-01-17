'''
# Definition of TreeNode
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
'''


def zigzagLevelOrder(root):
	# Base variables and inits
	answer, buff = [], []
	currStack, nextStack = [], []
	currStack.append(root)
	# if True move zig l to r else move zag r to l
	switch = False

	while currStack:
        # Pop current root
		node = currStack.pop()
		
        # Based on level that is zig or zag push left and right
		if switch:
			if node.right:
				nextStack.append(node.right)
			if node.left: 
				nextStack.append(node.left)
		else:
			if node.left:
				nextStack.append(node.left)
			if node.right:
				nextStack.append(node.right)
        # Store the level order in buff
		buff.append(node.val)
        # When currStack is empty, store current level buff into answer
        # Empty buff, switch zig zag, swap current with nextStack
		if len(currStack) == 0:
			answer.append(buff)
			buff, switch = [], not switch
			currStack,nextStack = nextStack, currStack
	return answer