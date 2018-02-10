class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi= nums[0]
        su= 0
        for i in nums:
            mi= min( mi, i)
            su+= i
        return ( su - mi*len(nums) )