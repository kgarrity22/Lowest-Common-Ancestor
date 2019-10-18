# # Testing LCA function
#
#
# # import the unittest function
import unittest
import LCA as lca
import networkx as nx
from binarytree import tree, bst, heap


# create class where we will write test functions
class TestLCA(unittest.TestCase):

    def test_simple_graph(self):
        # test a simple directed acyclic graph with three nodes

        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3])
        G.add_edges_from([(1, 2), (2, 3)])

        result = lca.LCA_total(G, 2, 3)
        expected = 2
        self.assertEqual(expected, result)

    def test_larger_graph(self):
        # test a slightly longer directed acyclic graph

        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (6, 7), (7, 8), (8, 9), (9, 10)])

        result = lca.LCA_total(G, 3, 3)
        expected = 3
        self.assertEqual(expected, result)


    def test_non_acyclic_graph(self):
        # test a non-acyclic graph (Node 5 connects back to Node 1)

        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5])
        G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)])

        result = lca.LCA_total(G, 5, 3)
        expected = False

        self.assertEqual(expected, result)

    def test_graph_with_invalid_input(self):
        # test for finding a node that is not in the graph

        G = nx.DiGraph()
        G.add_nodes_from([2, 4, 6, 8, 10])
        G.add_edges_from([(2, 4), (4, 6), (6, 8), (8, 10)])

        result = lca.LCA_total(G, 5, 7)
        expected = "The node you are looking for is not in the graph."

        self.assertEqual(expected, result)

    def test_complicated_dag(self):
        # test complex directed acyclic graph

        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        G.add_edges_from([(1, 5), (1, 9), (2, 6), (2, 10), (3, 7), (4, 8), (4, 12)])
        G.add_edges_from([(5, 13), (9, 14), (6, 13), (10, 14), (7, 13), (11, 14), (8, 13), (12, 14)])

        result = lca.LCA_total(G, 5, 8)
        expected = None

        self.assertEqual(result, expected)

        result2 = lca.LCA_total(G, 13, 6)
        expected2 = 6
        self.assertEqual(expected2, result2)

    def test_for_multiple_nodes(self):
        # test search for more than 2 nodes (set to return error message)

        G = nx.DiGraph()
        G.add_nodes_from([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
        G.add_edges_from([(1, 5), (1, 9), (2, 6), (2, 10), (3, 7), (4, 8), (4, 12)])
        G.add_edges_from([(5, 13), (9, 14), (6, 13), (10, 14), (7, 13), (11, 14), (8, 13), (12, 14)])

        result = lca.LCA_total(G, 14, 12, 8)
        expected = "Cannot compute lca of more than two nodes."
        self.assertEqual(expected, result)

        result2 = lca.LCA_total(G, 13, 14, 11)
        expected2 = "Cannot compute lca of more than two nodes."

        self.assertEqual(expected2, result2)



    def test_regular_tree(self):
        # test simple tree

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(root, root.right.left, root.right.right)
        expected = root.right

        # check for expected output
        self.assertEqual(expected, result)


    def test_lca_as_root(self):
        # test a tree where the LCA is the root node

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(root, root.right.left, root.left.left)
        expected = root

        self.assertEqual(expected, result)


    def test_LCA_for_input_not_in_tree(self):
        # test for nodes that aren't in the tree

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(root, root.right.right.right, root.right.left.left)
        expected = False

        self.assertEqual(expected, result)


    def test_only_right_tree(self):
        # test a tree with only right nodes

        root = lca.Node(2)
        root.right = lca.Node(3)
        root.right.right = lca.Node(7)
        root.right.right.right = lca.Node(18)
        root.right.right.right.right = lca.Node(24)
        root.right.right.right.right.right = lca.Node(900)

        result = lca.LCA_total(root, root.right.right.right, root.right.right.right.right)
        expected = root.right.right.right

        self.assertEqual(expected, result)


    def test_only_left_tree(self):
        # test a tree with only left nodes

        root = lca.Node(7)
        root.left = lca.Node(65)
        root.left.left = lca.Node(3)
        root.left.left.left = lca.Node(92)
        root.left.left.left.left = lca.Node(17)
        root.left.left.left.left.left = lca.Node(37)

        result = lca.LCA_total(root, root.left.left, root.left.left.left.left)
        expected = root.left.left

        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, root.left.left, root.left.left.left)
        expected2 = root.left.left
        self.assertEqual(expected2, result2)


    def test_empty_tree(self):
        # test a tree with no values

        root = lca.Node(None)
        result = lca.LCA_total(root, root.left, root.right)
        expected = False

        self.assertEqual(expected, result)


    def test_string_tree(self):
        # test tree with strings as node values

        root = lca.Node("pizza")
        root.left = lca.Node("Software Engineering")
        root.right = lca.Node("autumn")
        root.left.left = lca.Node("Alaska")
        root.left.right = lca.Node("salt")
        root.right.left = lca.Node("city")
        root.right.right = lca.Node("sidewalk")

        result = lca.LCA_total(root, root.right.left, root.left)
        expected = root

        self.assertEqual(expected, result)

        result2 = lca.LCA_total(root, root.left.right, root.left.left)
        expected2 = root.left

        self.assertEqual(expected2, result2)

    def test_tree_with_list_nodes(self):
        # test tree with lists as node values

        root = lca.Node([12, 7, 8, 100])
        root.left = lca.Node([1, "blacksmith", "July", 4])
        root.right = lca.Node([])
        root.left.left = lca.Node([13, ["purple"], 3456])
        root.left.right = lca.Node(["15", 15, 88])
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(["last"])

        result = lca.LCA_total(root, root.right.left, root.right.right)
        expected = root.right

        self.assertEqual(expected, result)


    def test_string_int_list_tree(self):
        # test tree with mixed string, int, lists as node values

        root = lca.Node(42)
        root.left = lca.Node("Software Engineering")
        root.right = lca.Node([1, "blacksmith", "July", 4])
        root.left.left = lca.Node(78)
        root.left.right = lca.Node("salt")
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(365)

        result = lca.LCA_total(root, root.right.right, root.left.right)
        expected = root

        self.assertEqual(expected, result)



    def test_tree_with_random_empty_nodes(self):
        # test tree with random nodes with None value

        root = lca.Node(100)
        root.left = lca.Node(None)
        root.right = lca.Node(3)
        root.left.left = lca.Node(38)
        root.left.right = lca.Node(None)
        root.right.left = lca.Node(3.4)
        root.right.right = lca.Node(None)
        root.right.right.right = lca.Node(95)
        root.right.left.right = lca.Node(7)
        root.left.right.left = lca.Node(None)
        root.left.right.left.left = lca.Node(46)

        result = lca.LCA_total(root, root.left.right.left.left, root.left.left)
        expected = root.left
        self.assertEqual(expected, result)

        result2 =lca.LCA_total(root, root.right.left.right, root.right.right.right)
        expected2 = root.right
        self.assertEqual(result2, expected2)



    def test_tree_with_invalid_findlca_input(self):
        # test tree where n1 or n1 is not Node type

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(root, "string", root.left.left)
        expected = False
        self.assertEqual(expected, result)


    def test_tree_with_one_none_input(self):
        # test tree where one node is None

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(root, root.right.right, None)
        expected = False

        self.assertEqual(expected, result)


    def test_search_for_all_None_inputs(self):
        # test tree where all input is None

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.LCA_total(None, None, None)
        expected = None

        result = lca.find_lca(root, root.left, root.left.right)
        expected = root.left
        self.assertEqual(expected, result)


    def test_tree_with_repeated_Nodes(self):
        # test tree with two nodes that have the same value

        root = lca.Node(6)
        root.left = lca.Node(4)
        root.right = lca.Node(40)
        root.left.left = lca.Node(32)
        root.left.right = lca.Node(67)
        root.right.left = lca.Node(32)
        root.right.right = lca.Node(999)


        result = lca.LCA_total(root, root.left, root.right.right)
        expected = root

        self.assertEqual(expected, result)

        result2 = lca.LCA_total(root, root.right, root.right.right)
        expected2 = root.right

        self.assertEqual(expected2, result2)


        result2 = lca.LCA_total(root, root.left.left, root.right.left)
        expected2 = root
        self.assertEqual(expected2, result2)


    def test_very_big_tree(self):
        # test binary tree of height 9

        root = tree(height=9)

        result = lca.find_lca(root, root.right.right.right.right, root.right.right.right.right.right.right.right)
        expected = root.right.right.right.right

        self.assertEqual(expected, result)


        result2 = lca.find_lca(root, root.left.left.right.left, root.left.left.left.right.right)
        expected2 = root.left.left

        self.assertEqual(expected2, result2)


    def test_tree_with_three_nodes(self):
        # test tree with three-nodes
        # this works for left and right nodes, but can't handle the center nodes

        root = lca.Node(79)
        root.left = lca.Node(389)
        root.right = lca.Node(2)
        root.center = lca.Node(10)

        root.left.left = lca.Node(36)
        root.left.right = lca.Node(37)
        root.left.center = lca.Node(29)

        root.right.left = lca.Node(0)
        root.right.right = lca.Node(15)
        root.right.center = lca.Node(89)

        root.center.right = lca.Node(213)
        root.center.left = lca.Node(713)
        root.center.center= lca.Node(23)

        result = lca.find_lca(root, root.left, root.right)
        expected = root

        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, root.center.right, root.center.center)
        expected2 = root.center
        self.assertEqual(expected2, result2)


    def test_lca_for_dag(self):
        # this is the tree test for DAGs
        # since I construct graphs differently, none of the tree test will work with graphs
        
        root = lca.Node("G")
        root.left = lca.Node("D")
        root.right = lca.Node("F")
        root.left.center = lca.Node("C")
        root.right.center = lca.Node("E")
        root.left.center.center = lca.Node("B")
        root.right.center.center = root.left.center.center
        root.left.center.center.center = lca.Node("A")

        result = lca.LCA_total(root, root.left.center.center, root.right.center)
        expected = root.right.center

        self.assertEqual(expected, result)



 # Test Runner

if __name__ == '__main__':
    unittest.main()
