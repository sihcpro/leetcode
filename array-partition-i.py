class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        s= 0
        for i in range(0,len( nums ) ):
            if i%2 == 0:
                s+= nums[i]
        return s