class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        m = sorted(nums)
        m.reverse()
        a= [ str( m.index(i)+1 ) for i in nums ]
        a[ a.index("1") ]= "Gold Medal"
        if len(a)>1: a[ a.index("2") ]= "Silver Medal"
        if len(a)>2: a[ a.index("3") ]= "Bronze Medal"
        return a