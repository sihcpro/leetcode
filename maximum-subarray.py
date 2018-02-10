class Solution(object):
    def maxSubArray(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """
        if n == []:
            return 0
        s= n[0]
        mini= n[0]
        maxi= n[0]
        for i in n:
            s+= i
            maxi= max(maxi, s-mini)
            mini= min(mini, s)
            # print( maxi )
        return maxi
        