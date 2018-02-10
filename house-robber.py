class Solution:
    def rob(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if n == []:
            return 0
        c=[]
        for i,j in enumerate(n):
            if i < 1:
                c.append( [n[0], 0] )
            else:
                c.append( [j+c[-1][1], max(c[-1])] )
        # print(c)
        return max(c[-1])