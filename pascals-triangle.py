class Solution:
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        a= []
        for i in range(n):
            if i == 0:
                a.append([1])
            else:
                b= []
                for j in range(len(a[i-1])-1):
                    b.append( a[i-1][j]+a[i-1][j+1] )
                a.append([1]+b+[1])
        return a
            
            
            