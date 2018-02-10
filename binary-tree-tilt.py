# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sum(self, root):
        if root == None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)
        
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return abs( self.sum(root.left) - self.sum(root.right) ) + self.findTilt(root.left) + self.findTilt(root.right)