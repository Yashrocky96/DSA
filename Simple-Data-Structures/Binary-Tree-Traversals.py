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
