class Solution:
    def isPowerOfFour(self, n):
        """
        :type num: int
        :rtype: bool
        """
        while n > 0 and n & 0x3 == 0:
            n >>= 2
            # print(n)
        return n == 1