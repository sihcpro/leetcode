class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        j= list(J)
        s= list(S)
        sum= 0
        for i in j:
            sum+= s.count( i )
            print( sum )
        return sum