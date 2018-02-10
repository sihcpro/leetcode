class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        a= [ [0 for j in M[0] ] for i in M]
        # b= [ [i[0] if j == 0 else i[j-1]+i[j] for j in range(0,len(i)) ] for i in M ]
        b= [ [0 for j in M[0] ] for i in M]
        
        for i, i2 in enumerate( M ):
            s= 0
            for j, j2 in enumerate( i2 ):
                s= a[i][j]= j2+s
        for i in a:
            i.insert(0,0)
        # print(a)
        n= len(M)
        m= len(M[0])
        for i, i2 in enumerate( a ):
            for j in range(0, len(i2)-1 ):
                # print("[ %s ; %s ]" %(i,j))
                # print("[ %s ; %s ]" %(min(n-1, j+2),max(0, j-1)))
                d= min(m, j+2) - max(0, j-1)
                s= a[ i ][ min(m, j+2) ] - a[ i ][ max(0, j-1) ]
                # print( str(s)+ "   "+str(d))
                if i > 0:
                    s+= a[ i-1 ][ min(m, j+2) ] - a[ i-1 ][ max(0, j-1) ]
                    d+= min(m, j+2) - max(0, j-1)
                # print( str(s)+ "   "+str(d))
                if i < n-1:
                    s+= a[ i+1 ][ min(m, j+2) ] - a[ i+1 ][ max(0, j-1) ]
                    d+= min(m, j+2) - max(0, j-1)
                # print( str(s)+ "   "+str(d))
                # print("--------------")
                b[i][j]= s//d
        return b
                    