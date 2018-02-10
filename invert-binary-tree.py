# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invert( self, root):
        if root == None:
            return
        root.left, root.right = root.right, root.left
        self.invert(root.left)
        self.invert(root.right)
    
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invert(root)
        return root