class Solution:
    def maxProfit(self, p):
        """
        :type prices: List[int]
        :rtype: int
        """
        if p == []:
            return 0
        s= p[-1]
        maxi= 0
        for i in p[::-1]:
            s= max(i, s)
            maxi= max( maxi, s - i )
            # print("%d %d %d" % (i, s, maxi))
        return maxi