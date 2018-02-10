class Solution:
    def addK(self, root, a):
        if root == None:
            return
        a.append( root.val )
        self.addK(root.left, a)
        self.addK(root.right, a)
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        a= []
        self.addK(root, a)
        a.sort()
        i= 0
        j= len(a)-1
        while i < j:
            if a[i] + a[j] == k:
                return True
            elif a[i] + a[j] < k:
                i+=1
            else:
                j-=1
        return False
        