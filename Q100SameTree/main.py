# 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Time and space complexity
# The time complexity of the isSameTree function is O(n), where n is the number of nodes in the binary tree. This is because the function recursively traverses each node in both trees once, comparing their values. In the worst case, where both trees have n nodes, the function will perform n comparisons.
# The space complexity of the isSameTree function is O(h), where h is the height of the binary tree. This is because the function uses the call stack to store the recursive function calls. In the worst case, where the binary tree is skewed and has a height of n, the function will have n recursive calls on the call stack.

# Example 1
# Input: p = [1,2,3], q = [1,2,3]
# Output: true


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: return True
        elif p is None and q is not None: return False
        elif q is None and p is not None: return False
        elif p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)