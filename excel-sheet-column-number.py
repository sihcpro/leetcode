class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s= list(s)
        sum= 0
        for i in range(0, len(s)):
            sum+= (ord(s[i])-ord("A")+1)* ( 26**(len(s)-i-1) )
            # print(sum)
        return sum