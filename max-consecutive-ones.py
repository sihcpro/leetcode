class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m= 0
        sn = [str(i) for i in nums]
        s= "".join(sn).split("0")
        # print(s)
        for i in s:
            m= max( m, len(i))
        return m