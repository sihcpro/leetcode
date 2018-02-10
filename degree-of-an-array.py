class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d= 0
        for i in set(nums):
            d2= nums.count(i)
            if d2 > d:
                d= d2
        mini= 50000
        for k in set(nums):
            if nums.count(k) == d:
                bg= -1
                ed= 0
                # print(k)
                for i, j in enumerate(nums):
                    if j == k:
                        if bg == -1:
                            bg= i
                        ed= i
                # print("%d %d" % (ed, bg))
                mini= min( mini, ed-bg+1)
                if mini == d:
                    return mini
        return mini
