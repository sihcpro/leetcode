class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z= x|y
        t= x&y
        k= list( bin(z) ).count('1') - list( bin(t) ).count('1')
        print( k )
        return k