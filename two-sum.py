class Solution:
    def twoSum(self, n, m):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,j in enumerate(n):
            if n.count(m-j) > 0 and n.index(m-j)!=i:
                return [i,n.index(m-j)]
        
        
        