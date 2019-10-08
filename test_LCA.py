# Testing LCA function

class Tree:
	def __init__(self):
		self.left = None
		self.right = None
		self.data = None

def create_tree(): ## this might work but it will involve inputing each data value - will take longer

	root = Tree()

# import the unittest function
import unittest
import LCA

# create class where we will write test functions
class TestLCA(unittest.TestCase):

    # Test if it works when neither node is in the tree
    def test_LCA_for_input_not_in_tree(self):

        # create the tree to be tested ** this needs to be changed

        root = Tree()

        root.data = 1
        root.left = Tree()
        root.left.data = 2
        root.right = Tree()
        root.right.data = 3
        root.left.left = Tree()
        root.left.left.data = 4
        root.left.right = Tree()
        root.left.right.data = 5
        root.right.left = Tree()
        root.right.left.data = 6
        root.right.right = Tree()
        root.right.right.data = 7

        # caputure the results of the function
        result = find_lca(root, 10, 4).data
        expected = None

        # check for expected output
        self.assertEqual(expected, result)


    def test_only_right_tree(self):
        # this function will make sure the LCA works for a tree with only right nodes

        root = Tree()
        root.data = 1
        root.right = Tree()
        root.right.data = 3
        root.right.right = Tree()
        root.right.right.data = 7
        root.right.right.right = Tree()
        root.right.right.right.data = 18
        root.right.right.right.right = Tree()
        root.right.right.right.right.data = 24
        root.right.right.right.right.right = Tree()
        root.right.right.right.right.right.data = 900

        result = find_lca(root, 18, 24).data
        expected = 18

        self.assertEqual(expected, result)



    # def test_only_left_tree(self):
        # this function will make sure the LCA works for a tree with only left nodes

        # root = create_tree()
        # root.left.data = Node(65)
        # root.left.left.data = Node(3)
        # root.left.left.left.data = Node(92)
        # root.left.left.left.left.data = Node(12)
        # root.left.left.left.left.left.data = Node(37)
        #
        # result = find_lca(root, 3, 17).data
        # expected = 17
        #
        # self.assertEqual(expected, result)

    #
    # def test_empty_tree(self):
    #     # testing LCA code for empty Tree
    #



# currently fails since there is no tree and there is no saved LCA function file




 # Test Runner

if __name__ == '__main__':
    unittest.main()
