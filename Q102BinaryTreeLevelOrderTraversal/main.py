# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Time complexity: O(n) where n is number of nodes
# Space complexity; O(n) where n is number of nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        list = []
        if root is None: return []
        def traverse(root, list, level):
            if root is None: return
            if level >= len(list):
                tempList = []
                tempList.append(root.val)
                list.append(tempList)
            else:
                list[level].append(root.val)
            traverse(root.left, list, level+1)
            traverse(root.right, list, level+1)
                
        traverse(root, list, 0)
        return list