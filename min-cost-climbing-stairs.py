class Solution:
    def minCostClimbingStairs(self, c):
        """
        :type cost: List[int]
        :rtype: int
        """
        a= [0,0]
        for i in range(1, len(c)):
            n= len(a)
            a.append( min( a[n-1]+c[i], a[n-2]+c[i-1] ) )
        return a.pop()