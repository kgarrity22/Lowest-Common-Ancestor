#LCA function
# Kathleen Garrity

# originally found on https://www.techiedelight.com/find-lowest-common-ancestor-lca-two-nodes-binary-tree/

# from binarytree import Node, tree, bst, heap, build
import binarytree
import networkx as nx
class Node:

	# A utility function to create a new node
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def __repr__(self):
		return str(self.data)

def LCA_total(structure, n1, n2):
	# if the structure is a tree do one thing
	if isinstance(structure, Node) or isinstance(structure, binarytree.Node):
		find_lca(structure, n1, n2)

	elif:
		# isinstance(structure, Graph):
		# find_lca_graph

def find_lca_graph(graph, n1, n2):
	# make sure the n1 and n2 are graph items
	

def lca(root, a, b):
    if not root: return None
    if root.value == a.value or root.value == b.value: return root
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
		if not isinstance(root, binarytree.Node) or not isinstance(n1, binarytree.Node) or not isinstance(n2, binarytree.Node):
			return False

	return lca(root, n1, n2)
