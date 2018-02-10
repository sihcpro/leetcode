# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def depth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return max(self.depth(root.left), self.depth(root.right)) + 1
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.depth(root)