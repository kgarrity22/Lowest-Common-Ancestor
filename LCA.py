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

def LCA_total(structure, *args):
	# if the structure is a tree do one thing
	if isinstance(structure, Node) or isinstance(structure, binarytree.Node):
		l = [item for item in args]
		n1 = l[0]
		n2 = l[1]
		return find_lca(structure, n1, n2)

	elif isinstance(structure, nx.Graph):
		return find_lca_graph(structure, *args)

def find_lca_graph(graph, *args):
	# if the graph is empty
	if not graph:
		return None

	if not nx.is_directed_acyclic_graph(graph):
		return False

	else:
		l = [item for item in args]
		for i in l:
			if i not in graph:
				return ("The node you are looking for is not in the graph.")
		if len(l)>2:
			return ("Cannot compute lca of more than two nodes.")
		return nx.lowest_common_ancestor(graph, *args)



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
