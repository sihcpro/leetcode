class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s.split()
        t.split()
        for i in range(ord('a'), ord('z')+1):
            if s.count(chr(i)) != t.count(chr(i)):
                return False
        return True

	def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s.split()
        s= "".join( sorted( s ) )
        t.split()
        t= "".join( sorted( t ) )
        # print(s)
        return s == t