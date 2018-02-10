# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, r, s, kt= False):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        t= False
        # t= True
        if r is None:
            if t: print("="+"null"+" 0 0")
            return 0
        if t: print( "%d %d %d" %(r.val, s, kt) )
        
        if kt == False: # bat dau 1 tong moi
            su= self.pathSum( r.left, s, False) + self.pathSum( r.right, s, False)
            su+= self.pathSum( r.left, s-r.val, True) + self.pathSum( r.right, s-r.val, True) 
            if r.val == s:
                return su+ 1
            else:
                if t: print("=     "+str(r.val)+" 1 " + str(sp))
                return su
        else:
            su= self.pathSum( r.left, s-r.val, True) + self.pathSum( r.right, s-r.val, True)
            if s == r.val:
                if t: print("=     "+str(r.val)+" 4 "+str(su+1))
                return su+1
            else:
                if t: print("=     "+str(r.val)+" 5 "+str(su))
                return su
