class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        s= 0
        for i in list( str(num) ):
            s+= int(i)
        return self.addDigits( s )