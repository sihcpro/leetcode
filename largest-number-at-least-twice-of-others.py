class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m= max(nums)
        if nums.count(m) != 1:
            return -1
        for i in nums:
            if i!= m and m < 2*i:
                return -1
        return nums.index(m)
