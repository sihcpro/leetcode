class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n= len(grid)
        m= len(grid[0])
        p= 0
        for i in range(0,n):
            for j in range(0,m):
                if grid[i][j] == 1:
                    s= 0
                    if i == 0 or grid[i-1][j] == 0:
                        s+= 1
                    if i == n-1 or grid[i+1][j] == 0:
                        s+= 1
                    if j == 0 or grid[i][j-1] == 0:
                        s+= 1
                    if j == m-1 or grid[i][j+1] == 0:
                        s+= 1
                    # print( str(i)+" "+str(j) +" = "+str(s))
                    p+= s
        return p
                    