# Testing LCA function



# import the unittest function
import unittest

# create class where we will write test functions
class TestLCA(unittest.TestCase):

    # Test if it works when neither node is in the tree
    def test_LCA_for_input_not_in_tree(self):

        # caputure the results of the function
        result = find_lca(root, n1, n2)
        expected = None

        # check for expected output
        self.assertEqual(expected, result)

# currently fails since there is no tree and there is no saved LCA function file




 # Test Runner

if __name__ == '__main__':
    unittest.main()
