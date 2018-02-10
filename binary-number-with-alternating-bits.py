class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        m= n>>1
        k= n|m
        print(n&m)
        print(k)
        if n & m == 0 and k+1 == 2**( len( str( bin(k) ) ) -2 ):
            return True
        else:
            return False