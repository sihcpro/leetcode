class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if words == []:
            return ""
        a= []
        for i in words:
            d= 0
            # print(i)
            for j in range(1,len(i)):
                # print( i[0:j] )
                # print( words.count( i[0:j] ) )
                if words.count( i[0:j] ) > 0:
                    d+= 1
                else:
                    break
            # print( d )
            if d == len(i)-1:
                a.append( [d, i] )
        print("sort")
        a.sort()
        # print( a )
        m= a[-1][0]
        s= ""
        for i,j in a:
            if i == m:
                return j
        