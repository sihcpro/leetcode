class Solution:
    def convertToBase7(self, n):
        """
        :type num: int
        :rtype: str
        """
        m= abs(n)
        s=""
        while m > 0:
            # print( "%s   %s" %( m%7, m//7) )
            s= str( m%7 )+s
            m//= 7
        if n < 0:
            s= "-"+s
        elif n == 0:
            s= "0"
        return s