# Testing LCA function



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
		expected = 0

		self.assertEqual(expected, result)




# currently fails since there is no tree and there is no saved LCA function file




 # Test Runner

if __name__ == '__main__':
    unittest.main()
