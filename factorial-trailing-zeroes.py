class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        n5= 0
        m5= 5
        while n >= m5:
            n5+= n//m5
            m5*= 5
        return n5
        
        
        