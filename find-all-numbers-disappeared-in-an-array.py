class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(0,len(nums)):
            # print("i= "+str(i+1))
            sp= nums[i]
            while sp != i+1 and nums[ sp-1 ] != nums[i]:
                nums[sp-1], sp= sp, nums[sp-1]
                nums[i]= sp
                # print(sp)
                # print(nums)
        a= []
        for i in range(0,len(nums)):
            if i+1 != nums[i]:
                a.append(i+1)
        return a