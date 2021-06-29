#DISC 05
import lab05
from lab05 import tree,is_leaf,branches,print_tree,label
"""
1.1 Write a function that returns the height of a tree. Recall that the height of
a treeis the length of the longest path from the root to a leaf.
"""
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 1
    return 1+ max(height(branch) for branch in branches(t))

"""
1.2 Write a function that takes in a tree and returns the maximum sum of the
values along any path in the tree. Recall that a path is from the tree’s root
to any leaf.
"""
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    return label(t) + max([max_path_sum(b) for b in branches(t)])

"""
1.3 Tutorial: Write a function that takes in a tree and squares every value. It should
return a new tree. You can assume that every item is a number.
"""
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                       [tree(6,
    ...                             [tree(7)]),
    ...                        tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
        4
            9
            16
        25
            36
                49
            64
    """
    return tree(label(t)**2, [square_tree(branch) for branch in branches(t)])


"""
1.4 Tutorial: Write a function that takes in a tree and a value x and returns a
list containing the nodes along the path required to get from the root of the
tree to a node containing x.
If x is not present in the tree, return None. Assume that the entries of the
tree are unique.
For the following tree, find path(t, 5) should return [2, 7, 6, 5]
"""
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [label(tree)]
    for b in branches(tree):
        path = find_path(b,x)
        if path:
            return [label(tree)]+path

"""
2.2 Write a function that takes in a tree consisting of ’0’s and ’1’s t and a list of ”binary
numbers” nums and returns a new tree that contains only the numbers in nums that
exist in t. If there are no numbers in nums that exist in t, return None.
Definition: Each binary number is represented as a string. A binary number n
exists in t if there is some path from the root to leaf of t whose values are equal to
n.
"""
def prune_binary(t,nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [n[1:] for n in nums if n[0] == label(t)]
        new_branches = []
        for b in branches(t):
            pruned_branch = prune_binary(b, next_valid_nums)
            if pruned_branch is not None:
                new_branches = new_branches + [pruned_branch]
        if not new_branches:
            return None
        return tree(label(t), new_branches)
