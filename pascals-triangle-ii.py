class Solution:
    def getRow(self, n):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if n == 0:
            return [1]
        a= [1]
        for i in range(1,n+1):
            a.append(0)
            sp1, sp2= 0, a[0]
            for j in range(1,i):
                sp1= a[j]
                a[j]= sp2+sp1
                sp2= sp1
            a[-1]= 1
        return a