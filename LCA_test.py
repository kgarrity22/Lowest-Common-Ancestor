# Testing LCA function



# import the unittest function
import unittest

# create class where we will write test functions
class TestLCA(unittest.TestCase):

    # Test if it works when neither node is in the tree
    def test_LCA_for_input_not_in_tree(self):

        # create the tree to be tested
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)

        # caputure the results of the function
        result = find_lca(root, 10, 4).data
        expected = None

        # check for expected output
        self.assertEqual(expected, result)

    #
    # def test_only_right_tree(self):
    #     # this function will make sure the LCA works for a tree with only right nodes
    #
    #
    # def test_only_left_tree(self):
    #     # this function will make sure the LCA works for a tree with only left nodes
    #
    #
    # def test_empty_tree(self):
    #     # testing LCA code for empty Tree



# currently fails since there is no tree and there is no saved LCA function file




 # Test Runner

if __name__ == '__main__':
    unittest.main()
