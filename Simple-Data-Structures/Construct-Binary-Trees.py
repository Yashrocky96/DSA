"""
Main I/O handled by problem maker
given function constructs a perfectBinaryTree of given depth
and returns in-order traversal
in O(n) time.
"""

from collections import deque
from crio.ds.Tree import TreeNode
"""
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

Use TreeNode.TreeNode(data) to create new Node
"""

# TODO: Implement this method
def perfectBinaryTree(depth):
	root = TreeNode.TreeNode(0)
	Q = deque()
	Q.append(root)
	while True:
		temp = Q.popleft()
		if temp.val == depth:
			return root

		# Create child nodes
		temp.left = TreeNode.TreeNode(temp.val + 1)
		temp.right = TreeNode.TreeNode(temp.val + 1)

		# Push them in queue
		Q.append(temp.left)
		Q.append(temp.right)
