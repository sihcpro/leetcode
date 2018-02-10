class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        n= len( nums )
        m= len( nums[0] )
        
        a= []
        if r*c != m*n or ( n == r and m == c ):
            return nums
        b= []
        for i in nums:
            for j in i:
                b.append(j)
        # print(b)
        for i in range(0,r):
            d= []
            for j in range(0,c):
                d.append(b[i*c+j])
            # print(d)
            a.append(d)
        return a