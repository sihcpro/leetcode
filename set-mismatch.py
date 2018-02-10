class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        b= [0 for i in nums]
        for i in nums:
            b[i-1]= 1
        # print(b)
        for i in nums:
            m= abs(i)-1
            nums[ m ] = -nums[ m ]
            # b[ abs(nums[ m ]) -1 ]= 1
        # print(nums)
        for i,j in enumerate(nums):
            if j > 0 and b[i] == 1:
                return [i+1, b.index(0) + 1]