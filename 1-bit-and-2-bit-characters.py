class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        b= [ str(i) for i in bits]
        s= "".join( b )
        s= s.replace('01', '0 1').replace('10', '1 0').split()
        s0= list( s[ len(s)-1 ] )
        if s0[0] == '1':
            return False
        if len(s0) > 1:
            return True
        if len(s) == 1:
            return True
        if len( s[len(s)-2] ) % 2 == 0:
            return True
        else:
            return False
        # print(s)