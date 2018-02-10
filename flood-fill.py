class Solution:
    def floodFill(self, a, i, j, n):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if n == a[i][j]:
            return a
        sp= a[i][j]
        a[i][j]= n
        if i > 0 and a[i-1][j] == sp:
            self.floodFill(a, i-1, j, n)
        if j > 0 and a[i][j-1] == sp:
            self.floodFill(a, i, j-1, n)
        if i < len(a)-1 and a[i+1][j] == sp:
            self.floodFill(a, i+1, j, n)
        if j < len(a[0])-1 and a[i][j+1] == sp:
            self.floodFill(a, i, j+1, n)
        return a