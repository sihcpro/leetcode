class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        g.reverse()
        s.sort()
        print(g)
        j= len(s) -1
        for i in g:
            if j >= 0 and i <= s[j]:
                # print( i )
                j-= 1
        # print(j)
        return len(s) - j -1