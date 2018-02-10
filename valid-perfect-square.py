class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        i, j=1, num//2
        while i <= j:
            mid= (i+j)//2
            if mid*mid == num:
                return True
            if mid*mid > num:
                j= mid-1
            else:
                i= mid+1
            # print("%d %d" %(i,j))
        return False