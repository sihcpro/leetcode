class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        print( bin(num) )
        return ( 2**(len( bin( num ) )-2)-1 ) ^ num