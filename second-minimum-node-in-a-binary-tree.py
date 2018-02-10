# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def makeList(self, r):
        if r is None:
            return []
        return [r.val] + self.makeList(r.left) + self.makeList(r.right)
        
        
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a= self.makeList(root)
        a= sorted( list( set(a) ) )
        if len(a) == 1:
            return -1
        else:
            return a[ 1 ]
        