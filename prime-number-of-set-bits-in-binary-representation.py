class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        a= [2,3,5,7,11,13,17,19,23,29,31,37]
        d= 0
        for i in range(L,R+1):
            if bin(i).count("1") in a:
                # print( bin(i).count("1") )
                d+= 1
        return d 