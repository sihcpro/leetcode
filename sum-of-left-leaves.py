# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root, left= False):
        """
        :type root: TreeNode
        :rtype: int
        """
        # print(root.val)
        if root == None:
            return 0
        if root.left == None and root.right == None:
            if left:
                return root.val
            else:
                return 0
        a= 0
        if root.left != None:
            a+= self.sumOfLeftLeaves(root.left, True)
        if root.right != None:
            a+= self.sumOfLeftLeaves(root.right)
        return a