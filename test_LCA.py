# # Testing LCA function
#
# # *** can run more than one test in the same function
#
# # import the unittest function
import unittest
import LCA as lca
from binarytree import tree, bst, heap, build


# create class where we will write test functions
class TestLCA(unittest.TestCase):

    def test_regular_tree(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(root, root.right, root.right.right)
        expected = root.right

        # check for expected output
        self.assertEqual(expected, result)


    def test_lca_as_root(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(root, root.right.left, root.left.left)
        expected = root

        self.assertEqual(expected, result)

    # Test if it works when neither node is in the tree
    def test_LCA_for_input_not_in_tree(self):

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        # caputure the results of the function
        result = lca.find_lca(root, root.right.right.right, root.left.right.left)
        expected = False

        # check for expected output
        self.assertEqual(expected, result)


    def test_only_right_tree(self):
        # this function will make sure the LCA works for a tree with only right nodes

        root = lca.Node(2)
        root.right = lca.Node(3)
        root.right.right = lca.Node(7)
        root.right.right.right = lca.Node(18)
        root.right.right.right.right = lca.Node(24)
        root.right.right.right.right.right = lca.Node(900)

        result = lca.find_lca(root, root.right.right.right, root.right.right.right.right)
        expected = root.right.right.right

        self.assertEqual(expected, result)


    def test_only_left_tree(self):
        # this function will make sure the LCA works for a tree with only left nodes

        root = lca.Node(7)
        root.left = lca.Node(65)
        root.left.left = lca.Node(3)
        root.left.left.left = lca.Node(92)
        root.left.left.left.left = lca.Node(17)
        root.left.left.left.left.left = lca.Node(37)

        result = lca.find_lca(root, root.left, root.left.left.left)
        expected = root.left
        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, root.left.left, root.left.left.left)
        expected2 = root.left.left
        self.assertEqual(expected2, result2)


    def test_empty_tree(self):
        root = None
        # this shouldn't really be allowed ...? FIX
        # testing LCA code for empty Tree

		# is this an empty tree or just nothing?
        result = lca.find_lca(root, root, root)
        expected = False
        self.assertEqual(expected, result)

# should this be allowed? because it isn't based on the way I initialize my nodes
    def test_tree_with_nothing(self): #this is not working
        root = lca.Node(None)

        result = lca.find_lca(root, root, root)
        expected = root

        self.assertEqual(expected, result)


    def test_string_tree(self):
        # test code for a tree with strings in nodes

        root = lca.Node("pizza")
        root.left = lca.Node("Software Engineering")
        root.right = lca.Node("autumn")
        root.left.left = lca.Node("Alaska")
        root.left.right = lca.Node("salt")
        root.right.left = lca.Node("city")
        root.right.right = lca.Node("sidewalk")

        result = lca.find_lca(root, root.right.left, root.left)
        expected = root

        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, root.left.right, root.left)
        expected2 = root.left

        self.assertEqual(expected2, result2)

    def test_tree_with_list_nodes(self):
        root = lca.Node([12, 7, 8, 100])
        root.left = lca.Node([1, "blacksmith", "July", 4])
        root.right = lca.Node([])
        root.left.left = lca.Node([13, ["purple"], 3456])
        root.left.right = lca.Node(["15", 15, 88])
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(["last"])

        result = lca.find_lca(root, root.right.left, root.right.right)
        expected = root.right

        self.assertEqual(expected, result)


    def test_string_int_list_tree(self):
        root = lca.Node(42)
        root.left = lca.Node("Software Engineering")
        root.right = lca.Node([1, "blacksmith", "July", 4])
        root.left.left = lca.Node(78)
        root.left.right = lca.Node("salt")
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(365)

        result = lca.find_lca(root, root.right.right, root.left.right)
        expected = root
        self.assertEqual(expected, result)



    def test_tree_with_random_empty_nodes(self):
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

        result = lca.find_lca(root, root.left.right.left.left, root.left.left)
        expected = root.left
        self.assertEqual(expected, result)

        result2 =lca.find_lca(root, root.right.left.right, root.right.right.right)
        expected2 = root.right
        self.assertEqual(result2, expected2)



    def test_tree_with_invalid_findlca_input(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca("string", root.right, root.left.left)
        expected = False
        self.assertEqual(expected, result)


    def test_tree_with_one_none_input(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(root, 7, None)
        expected = False

        self.assertEqual(expected, result)


    def test_search_for_all_None_inputs(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(None, None, None)
        expected = False
        self.assertEqual(expected, result)


    def test_tree_with_repeated_Nodes(self):

        root = lca.Node(6)
        root.left = lca.Node(4)
        root.right = lca.Node(40)
        root.left.left = lca.Node(32)
        root.left.right = lca.Node(67)
        root.right.left = lca.Node(32)
        root.right.right = lca.Node(999)


        result = lca.find_lca(root, root.left, root.left.right)
        expected = root.left
        self.assertEqual(expected, result)


        result2 = lca.find_lca(root, root.left.left, root.right.left)
        expected2 = root
        self.assertEqual(expected2, result2)


    def test_very_big_tree(self):
        root = tree(height=9)


        result = lca.find_lca(root, root.right.right.right.right, root.right.right.right.right.right.right.right)
        expected = root.right.right.right.right

        self.assertEqual(expected, result)


        result2 = lca.find_lca(root, root.left.left.right.left, root.left.left.left.right.right)
        expected2 = root.left.left

        self.assertEqual(expected2, result2)

# this works for left and right nodes, but can't handle the center nodes
    def test_tree_with_three_nodes(self):
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
        root = lca.Node("G")
        root.left = lca.Node("D")
        root.right = lca.Node("F")
        root.left.center = lca.Node("C")
        root.right.center = lca.Node("E")
        root.left.center.center = lca.Node("B")
        root.right.center.center = root.left.center.center
        root.left.center.center.center = lca.Node("A")

        result = lca.find_lca(root, "B", "E").data
        expected = "E"

        self.assertEqual(expected, result)





 # Test Runner

if __name__ == '__main__':
    unittest.main()
