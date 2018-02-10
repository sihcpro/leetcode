class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        n= len( matrix )
        m= len( matrix[0] )
        for i in range( 0, n ):
            for j in range( 0, m ):
                # print( str(i+j) + " "+ str(j) )
                if i+j >= n:
                    break
                if matrix[i+j][j] != matrix[i][0]:
                    return False
        
        for i in range( 0, m ):
            for j in range( 0, n ):
                # print( str(i+j) + " "+ str(j) )
                if i+j >= m:
                    break
                if matrix[j][i+j] != matrix[0][i]:
                    return False
        
        
        return True