class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 0
        d= 1
        l= nums[0]
        maxi= 0
        for i in nums:
            if i <= l:
                maxi= max(maxi, d)
                d= 1
            else:
                d+= 1
            l= i
        return max( d, maxi)