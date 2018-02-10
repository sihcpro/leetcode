class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a= [0]
        d= [0,0]
        last= 0
        for i in s:
            i= int(i)
            if i == last:
                d[i]+= 1
            else:
                a.append( d[1-i] )
                d[1-i]= 0
                d[i]= 1
                last = i
        a.append( max(d[0], d[1]) )
        
        s= 0
        for i in range(1, len(a)):
            s+= min( a[i-1], a[i] )
        
        return s