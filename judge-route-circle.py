class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        m= list( moves )
        l= m.count('L')
        r= m.count('R')
        u= m.count('U')
        d= m.count('D')
        l-= r
        u-= d
        if l == 0 and u == 0:
            return True
        else:
            return False