# a   0010110101
# b   0010100111
#     ----------
# |   0010110111    c= a|b
# &   0010100101    d= a&b
# ^   0000010010    e= a^b
# <<& 0101001010    f= d<<1
# a   0101011010    a= e|f
# b   0000000010    b= e&f
#     ----------
# |   0101011010
# &   0000000010
# ^   0101011000
# <<& 0000000100
# a   0101011100
# b   0000000000

class Solution:
    def getSum(self, a, b): # 10, 11
        """
        :type a: int 1010
        :type b: int 1011
        :rtype: int
        """
        # print( str(bin(a))+" "+str(bin(b)))
        if( a*b < 0 ):
            c= min(a,b)
            b= max(a,b)
            a= c
            if( -a == b ):
                return 0
            elif( -a < b ):
                return - self.getSum( -a, -b )
        
        while b != 0:
            c= a|b
            d= a&b
            e= a^b
            f= d<<1
            a= e|f
            b= e&f
            # print(str(c)+" "+str(d)+" "+str(e)+" "+str(f)+" "+str(a)+" "+str(b))
        return a
    
        # c= list( str( bin( a|b ) ) )
        # c[1]= '0'
        # print(c)
        # a= list( str( bin( a&b ) ) )
        
        # d= 0
        # for i in range(len(c)-1, -1, -1):
        #     print(i)
        #     if d != 0 or a[i] != 0:
        #         b= c[i] | d&a[i]
        #         c[i] = c[i] ^ d ^ a[i]
        #         d= b
        
        # c= "".join(c)
        # return int(c,2)