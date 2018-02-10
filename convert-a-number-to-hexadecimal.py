class Solution:
    def toHex(self, n):
        """
        :type num: int
        :rtype: str
        """
        if n == 0:
            return "0"
        a= {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        d= 0
        s= ""
        while n != 0 and d < 32:
            b= n & 0xf
            if b < 10:
                s+= str(b)
            else:
                s+= a[b]
            d+= 4
            n >>= 4
        return s[::-1]