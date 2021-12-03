'''
In-order, Pre- and Post-traversal for a given root pointer of Binary Tree
Main I/O are handled
'''

'''
# Definition of TreeNode
class TreeNode:
	def __init__( val):
		val = val
		left = None
		right = None
'''

# Function for their respective traversal methods

def inorderTraversal(root):
	inorder = list()
	if root:
		inorder = inorderTraversal(root.left)
		inorder.append(root.val)
		inorder = inorder + inorderTraversal(root.right)

	return inorder

def preorderTraversal(root):
	preorder = list()
	if root:
		preorder.append(root.val)
		preorder += preorderTraversal(root.left)
		preorder += preorderTraversal(root.right)

	return preorder

def postorderTraversal(root):
	postorder = list()
	if root:
		postorder = postorderTraversal(root.left)
		postorder += postorderTraversal(root.right)
		postorder.append(root.val)

	return postorder

'''
Searches a Binary for a given value of k
'''
def binaryTreeSearching(root, k):
	# As we check nodes first and then recur
	search = False
	if root:
		if root.val == k:
			search = True
		if binaryTreeSearching(root.left, k):
			search = True
		if binaryTreeSearching(root.right, k):
			search = True
	return search

'''
Deletes all leaf nodes in a given binary tree
'''

def binaryTreeDeletion(root):
	if root:
		if root.left is None and root.right is None:
			return None
		root.left = binaryTreeDeletion(root.left)
		root.right = binaryTreeDeletion(root.right)
	return root

'''
Does Level Order Traversal and outputs each level values
in a separate line
'''

def binaryTreeLevelOrderTraversal(root):
	if root is None:
		return []
	Q = deque()
	Q.append(root)
	res = []
	while Q:
		buff = []
		for i in range(len(Q)):
			temp = Q.popleft()
			buff.append(temp.val)
			# Push childs in queue
			if temp.left:
				Q.append(temp.left)
			if temp.right:
				Q.append(temp.right)
		res.append(buff)
	return res
