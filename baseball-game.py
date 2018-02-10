class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        a= [0]
        for i in ops:
            if i == '+':
                sp2= a.pop()
                sp+= a[ len( a )-1 ]
                a.append( sp2 )
            elif i == 'D':
                sp= 2*a[ len( a )-1 ]
            elif i == 'C':
                a.pop()
                sp= a.pop()
            else:
                sp= int( i )
            print( i )
            a.append( sp )
        sum= 0
        for i in a:
            sum+= i
        return sum