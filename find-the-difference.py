class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s= sorted( list(s) )
        t= sorted( list(t) )
        for i in range(0,len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[ len(t) - 1 ]