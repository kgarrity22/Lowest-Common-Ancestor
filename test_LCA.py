# Testing LCA function

# *** can run more than one test in the same function

# import the unittest function
import unittest
import LCA as lca


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

        result = lca.find_lca(root, 6, 7).data
        expected = 3

        # check for expected output
        self.assertEqual(expected, result)

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



    def test_tree_with_random_empty_nodes(self):


        root = lca.Node(100)
        root.left = lca.Node()
        root.right = lca.Node(3)
        root.left.left = lca.Node(38)
        root.left.right = lca.Node()
        root.right.left = lca.Node(3.4)
        root.right.right = lca.Node()
        root.right.right.right = lca.Node(95)
        root.right.left.right = lca.Node(7)
        root.left.right.left = lca.Node()
        root.left.right.left.left = lca.Node(46)

        result = lca.find_lca(root, 46, 38).data
        expected = None

        self.assertEqual(expected, result)

        result2 = lca.find_lca(root, 7, 95).data
        expected2 = 3


# NOTE this ia a unique case where it doesn't work if we have None as the second input, but it will give us the
        result3 = lca.find_lca(root, root.left, 38).data
        expected3 = None

        self.assertEqual(expected3, result3)





# i dont know if we have to succeed with this function or not but i'll check with david
    def test_tree_where_you_dont_call_root_but_call_its_value_instead(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(lca.Node(1), 6, 7).data
        expected = 3

        self.assertEqual(expected, result)
# okay this fails when you don't call root in the finc_lca function... is this an issue or just required syntax?
# maybe should have a statement that deals with incorrect input?

    def test_tree_with_one_none_input(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(root, 7, None).data
        expected = None

        self.assertEqual(expected, result)

    def test_search_for_None_inputs(self):
        root = lca.Node(1)
        root.left = lca.Node(2)
        root.right = lca.Node(3)
        root.left.left = lca.Node(4)
        root.left.right = lca.Node(5)
        root.right.left = lca.Node(6)
        root.right.right = lca.Node(7)

        result = lca.find_lca(None, None, None).data
        expected = None

        self.assertEqual(expected, result)

# ****LCA fails when there are two of the same Node value -
## maybe doesn't matter what it does as long as it does what we want it to do?

    def test_tree_with_repeated_Nodes(self):
        # what do we want it to do? take the first parent or the second parent?

        root = lca.Node(6)
        root.left = lca.Node(4)
        root.right = lca.Node(40)
        root.left.left = lca.Node(32)
        root.left.right = lca.Node(67)
        root.right.left = lca.Node(32)
        root.right.right = lca.Node(999)


        result = lca.find_lca(root, 4, 32).data
        expected = 4 # if we are looking at the 32 that is a child of 4
        other_expected = 1 # if we are looking at the other 32

        self.assertEqual(expected, result)
        self.assertEqual(other_expected, result)



        result2 = lca.find_lca(root, 32, 32).data #check what will happen with this if there is only one 32
        expected2 = 1

        self.assertEqual(expected2, result2)


    # def test_tree_with_three_repeated_Nodes(self):
    #
    #     result = lca.find_lca(root, 32, 32).data # where there is 3 32's in the chart
    #




    # def test_very_big_tree(self):
    #     root = lca
    #     for i in range 100:
    #
    #     for j in range(101,200):








 # Test Runner

if __name__ == '__main__':
    unittest.main()
