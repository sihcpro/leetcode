class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n= int( (len(nums)+1)/2 )
        for i in set(nums):
            if nums.count(i) >= n:
                return i