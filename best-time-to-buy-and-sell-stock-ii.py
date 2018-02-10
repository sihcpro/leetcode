class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices.reverse()
        # print(prices)
        maxi= 0
        best= 0
        for i in prices:
            if( maxi-i > 0):
                best+= maxi-i
                maxi= i
            else:
                maxi= max(i, maxi)
        return best
        