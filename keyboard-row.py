class Solution(object):
    # a= ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"]
    # b= ["A", "S", "D", "F", "G", "H", "J", "K", "L"]
    # c= ["Z", "X", "C", "V", "B", "N", "M"]
    def checkA( self, word):
        a= "QWERTYUIOP"
        for i in word:
            if a.count( i ) == 0:
                return False
        return True
    def checkB( self, word):
        b= "ASDFGHJKL"
        for i in word:
            if b.count( i ) == 0:
                return False
        return True
    def checkC( self, word):
        c= "ZXCVBNM"
        for i in word:
            if c.count( i ) == 0:
                return False
        return True
    
    
    def check( self, word):
        return self.checkA(word.upper()) or self.checkB(word.upper()) or self.checkC(word.upper())
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a= []
        for i in words:
            if self.check( i ):
                a.append( i )
        return a