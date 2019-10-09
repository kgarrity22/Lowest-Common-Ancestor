# Testing LCA function

# *** can run more than one test in the same function

# import the unittest function
import unittest
import LCA as lca


# create class where we will write test functions
class TestLCA(unittest.TestCase):

    # Test if it works when neither node is in the tree
    def test_LCA_for_input_not_in_tree(self):

        # create the tree to be tested

        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        # caputure the results of the function
        result = lca.find_lca(root, 10, 4).data
        expected = None

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

        result = lca.find_lca(root, 18, 24).data
        expected = 18

        self.assertEqual(expected, result)



    def test_only_left_tree(self):
        # this function will make sure the LCA works for a tree with only left nodes

        root = lca.Node(7)
        root.left = lca.Node(65)
        root.left.left = lca.Node(3)
        root.left.left.left = lca.Node(92)
        root.left.left.left.left = lca.Node(17)
        root.left.left.left.left.left = lca.Node(37)

        result = lca.find_lca(root, 3, 17).data
        expected = 17

        self.assertEqual(expected, result)


    def test_empty_tree(self):
        # testing LCA code for empty Tree
		root = lca.Node(None)

		# is this an empty tree or just nothing?
		result = lca.find_lca(root, root, root).data
		expected = None

		self.assertEqual(expected, result)

# should this be allowed? because it isn't based on the way I initialize my nodes
    def test_tree_with_nothing(self): #this is not working
		root = lca.Node()

		result = lca.find_lca(root, root, root).data
		expected = None

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

        result = lca.find_lca(root, "city", "Software Engineering").data
        expected = "pizza"

        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, "salt", "Alaska").data
        expected2 = "Software Engineering"

        self.assertEqual(expected2, result2)

    def test_tree_with_list_nodes(self):
        root = lca.Node([12, 7, 8, 100])
        root.left = lca.Node([1, "blacksmith", "July", 4])
        root.right = lca.Node([])
        root.left.left = lca.Node([13, ["purple"], 3456])
        root.left.right = lca.Node(["15", 15, 88])
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(["last"])

        result = lca.find_lca(root, ["North", 74, 98, 0, "00", "001Court"], ["last"]).data
        expected = []

        self.assertEqual(expected, result)


    def test_string_int_list_tree(self):
        root = lca.Node(42)
        root.left = lca.Node("Software Engineering")
        root.right = lca.Node([1, "blacksmith", "July", 4])
        root.left.left = lca.Node(78)
        root.left.right = lca.Node("salt")
        root.right.left = lca.Node(["North", 74, 98, 0, "00", "001Court"])
        root.right.right = lca.Node(365)

        result = lca.find_lca(root, 365, "salt").data
        expected = 42

        self.assertEqual(expected, result)



    # def test_tree_with_random_empty_nodes(self):


    # def test_tree_where_you_dont_call_root_but_call_its_value_instead(self):
    #         # i dont know if we have to succeed with this function or not but i'll check with david
    #
    #



# currently fails since there is no tree and there is no saved LCA function file




 # Test Runner

if __name__ == '__main__':
    unittest.main()
