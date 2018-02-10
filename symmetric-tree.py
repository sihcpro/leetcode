# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def arr(self, r):
        if r is None:
            return [None]
        return ["|"] + self.arr(r.left) + [r.val] + self.arr(r.right) + ["|"]
    
    
    def isSymmetric(self, r):
        """
        :type root: TreeNode
        :rtype: bool
        """
        a= self.arr(r)
        # print(a)
        return a==a[::-1]