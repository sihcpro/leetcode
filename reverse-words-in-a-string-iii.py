class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == "":
            return ""
        x= "".join(reversed(s)).split()
        s= ""
        for i in range( 1, len(x) ):
            s= x[i]+" "+s
        s= s+x[0]
        # print( x )
        return s
                   