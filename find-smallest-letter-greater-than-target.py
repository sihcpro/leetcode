class Solution:
    def nextGreatestLetter(self, s, c):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        d= ord( c ) - ord( 'a' )
        for i in range(1, 27):
            if s.count( chr( ( d + i )%26 + ord('a') ) ) > 0:
                return  chr( ( d + i )%26 + ord('a') )
        