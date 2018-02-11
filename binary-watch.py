class Solution:
    def readBinaryWatch(self, n):
        """
        :type num: int
        :rtype: List[str]
        """
        a= []
        for i in range(0,12*60):
            m= i%60
            h= i//60
            d= ( bin(h)+bin(m) ).count("1")
            if d == n:
                s= str(h)+":"
                s2= str(m)
                if m < 10:
                    s2= "0"+s2
                a.append( s + s2 )
                # print(a)
        return a