class Solution:
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        a=""
        if t == None:
            return a
        a= str(t.val)
        if( t.left != None or t.right != None ):
            a+= "(" + self.tree2str(t.left) + ")"
        if t.right != None:
            a+= "(" + self.tree2str(t.right) + ")"
        return a