class Solution(object):
    def check(self, num ):
        s= list( str(num) )
        for i in s:
            if int(i) == 0 or num % int(i) != 0:
                return False
        return True
    
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        a= []
        for i in range(left, right+1):
            if self.check( i ):
                print(i)
                a.append(i)
        return a