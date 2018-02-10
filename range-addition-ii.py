class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minM= m
        minN= n
        for i in ops:
            minM= min( minM, i[0])
            minN= min( minN, i[1])
        return minN*minM