# CS3012 Software Engineering

## Fall 2019

### Kathleen Garrity


***

The task for this project is to  provide a program solution to the Lowest Common Ancestor problem.

For this particular project, we are working under the assymption that the graph is structured as a binary tree.

The instructions for this project are as follows

*   Choose a unit testing framework
*   Create a repository on a git service
*   Define a set of initial unit tests that capture the basic expected behavior by creating sample data and identifying the basic API for the LCA solution
*   Build the initial solition testing it against the test code until it is working
*   Refine the solution, expanding the test cases to deal with awkward parameters and edge cases that push the limits of the solution, enhacing the solution to deal with these cases

***
***
For the first piece of this project, I created tress as sets of connected Nodes, occassionally using the binarytree library for more complex trees.

For the second part of the project, I used the networkx library to created graphs. Since the graphs and trees are of different types, the test cases for the trees do not apply to the graphs and vice versa.

All but two of the tests succeed currently. The two that fail are test of a tree with three-nodes (a left, right and center node) and the test that attempted to constuct a DAG in the same format as a tree.
***
