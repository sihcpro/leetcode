class Solution
    def longestPalindrome(self, s)
        
        type s str
        rtype int
        
        d= 0
        su= 0
        for i in range(0,26)
            if d == 0 and ( s.count( chr(ord('a')+i) )%2 == 1 or s.count( chr(ord('A')+i) )%2 == 1 )
                d= 1
            su+= s.count( chr(ord('a')+i) )2 + s.count( chr(ord('A')+i) )2
        return 2su+d