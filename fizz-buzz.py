class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        a= []
        for i in range( 1, n+1):
            if i % 3 == 0:
                s= "Fizz"
            elif i % 5 != 0:
                s= str(i)
            else:
                s= ""
            if i % 5 == 0:
                s+= "Buzz"
            a.append(s)
        return a