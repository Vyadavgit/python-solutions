# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.

# Example:
# Input: root = [2,1,3]
# Output: true

# Time complexity: O(n) n = number of nodes in a tree
# Space complexity: O(h) h = height of tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(root, min_val, max_val):
            if root is None: return True
            if root.val <= min_val or root.val >= max_val: return False
            return recurse(root.left, min_val, root.val) and recurse(root.right, root.val, max_val)
        return recurse(root, float('-inf'), float('inf'))