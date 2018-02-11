class Solution:
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        n= len(nums)
        return nums[n-1] * max( nums[n-2]*nums[n-3], nums[0]*nums[1] )
    