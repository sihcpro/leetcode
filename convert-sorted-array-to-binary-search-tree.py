# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        n = len(nums)
        mid = n//2
        # print(nums[mid])
        r= TreeNode(nums[mid])
        # print( nums )
        # print( "%d | mid= %d | len= %d " %(r.val, mid, n) )
        if mid > 0:
            r.left= self.sortedArrayToBST( nums[0:mid])
        if mid+1 < n:
            r.right= self.sortedArrayToBST( nums[mid+1:n])
        return r