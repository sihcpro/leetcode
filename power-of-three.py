class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # print(math.log(n)/math.log(3))
        return n>0 and 3**int( round( math.log(n)/math.log(3) ) ) == n