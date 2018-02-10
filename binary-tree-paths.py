# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, r):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if r is None:
            return []
        a= self.binaryTreePaths(r.left) + self.binaryTreePaths(r.right)
        if a == []:
            a.append(str(r.val))
        else:
            # print("cong them")
            for i in range(0, len(a)):
                a[i]= str( r.val ) + "->" + a[i]
                # print(i)
        # print(r.val)
        # print(a)
        return a
        