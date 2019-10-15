#LCA function
# Kathleen Garrity

# originally found on https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/

from binarytree import Node, tree, bst, heap, build

class Node:

	# A utility function to create a new node
	def __init__(self, data, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

		#for creating a three-node
		self.center = None

	def __repr__(self):
		return str(self.data)


count = 0

def repeats(root, n1, count):
	if root.data == n1:
		count += 1
	if root.left:
		repeats(root.left, n1, count)
	if root.right:
		repeats(root.right, n1, count)

	if count > 1:
		return True
	# so if there are more than 1 nodes with the same value, this function will return true
	# now we want to run this on each node before we find the lca and if it is true, we need to find the LCA of each one
	# should try to tag each repeat as we find it

# def create_three_node(root, x, y, z):
#
# 	root.left = Node(x)
# 	root.right = Node(y)
#     root.center = Node(z)
# 	# need to update this


# This function returns pointer to LCA of two given values n1 and n2
# This function also verify that n1 and n2 are present in Binary Tree


def findLCA(root, n1, n2):
	# iterations = 1
	#
	# icrement = iterations+1
	# if icrement ==1:
	# 	if str(type(root)) != "class '__main__.Node'":
	# 		return("Invalid Input")

	if not root:
		# if the root is false, return false
		# print("this is what not root does: ")
		return root

	# findLCA.n1 and findLCA.n2 are boolean variables to verify nodes exists in tree.
	# Current node Match n1
	# if the root is the first node, findn1 is true, n1 has been found
	if root == n1:
		findLCA.n1 = True

	# Current node Match n2
	# if the root is the second input node, then n2 has been found
	if root == n2:
		findLCA.n2 = True

	# Both have been Matched no need to go any further.
	# This condition is added for scenario where both nodes are found no need to
	# further down the tree.
	# if
	if findLCA.n1 and findLCA.n2:
		return root

	# if lca_left not null atleast one of the nodes is present in left sub tree
	lca_left = findLCA(root.left, n1, n2)

	# Both have been Matched no need to go any further
	if findLCA.n1 and findLCA.n2:
		return lca_left

	# if lca_right not null at least one of the nodes is present in right sub tree
	lca_right = findLCA(root.right, n1, n2)

	# This condition is added for scenario where one of the requested node is LCA
	# Here we will override the child result received from parent node
	if root == n1 or root == n2:
		return root

	# if one node is present in left subtree and other in right subtree.
	# this will be your lowest common ancestor
	if lca_left and lca_right:
		return root

	if repeats(root, n1, 0):
		print("This node value ", n1, "occurs more than once.")
	if repeats(root, n2, 0):
		print("This node value ", n2, "occurs more than once.")




	# if there are two nodes with the same value in the tree
	# how do we scan the tree to see if the node appears twice? - should do this at the beginning

	# return if any of the subtree returned a result
	return lca_right if lca_right else lca_left

# This Methods finds Lca and also verify both node are present in tree
def find_lca(root, n1, n2):
	findLCA.n1 = False
	findLCA.n2 = False
	lca = findLCA(root, n1, n2)
	if findLCA.n1 and findLCA.n2:
		return lca
	# elif (lca == "Invalid Input"):
	# 	return lca
	else:
		return Node(None)

# functions for more easliy creating a very big Tree
#
# def add_right_Nodes(root, values, i):
# 	while i < len(values):
# 		root.right = Node(values[i])
# 		i += 1
# 		add_right_Nodes(root.right, values, i)
#
#
# def add_left_Nodes(root, values, i):
# 	while i < len(values):
# 		root.left = Node(values[i])
# 		i += 1
# 		add_right_Nodes(root.left, values, i)
