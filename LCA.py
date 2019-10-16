#LCA function
# Kathleen Garrity

# originally found on https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/

from binarytree import Node, tree, bst, heap, build

class Node:

	# A utility function to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.data)

# This function returns pointer to LCA of two given values n1 and n2
# This function also verify that n1 and n2 are present in Binary Tree

def lca(root, a, b):
    if not root: return None
    if root.data == a.data or root.data == b.data: return root
    left = lca(root.left, a, b)
    right = lca(root.right, a, b)
    if left and right:
        # a & b are on both sides
        return root
    else:
        # EITHER a/b is on one side
        # OR a/b is not in L&R subtrees
        return left if left else right


def find_lca(root, n1, n2):

	if not isinstance(root, Node) or not isinstance(n1, Node) or not isinstance(n2, Node):
		return False

	return lca(root, n1, n2)
