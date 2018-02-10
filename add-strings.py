class Solution:
    def addStrings(self, n1, n2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        a= {}
        for i in range(0,10):
            a[ str(i) ]= i
        s= ""
        d= 0
        for i,j in zip(n1[::-1], n2[::-1]):
            s+= str( ( a[i] + a[j] + d )%10 ) 
            d= ( a[i] + a[j] + d )//10
        m= abs(len(n1)-len(n2))
        if m > 0:
            if len(n1) > len(n2):
                l= len(n1) - len(n2)
                s2= n1[0:l]
            else:
                l= len(n2) - len(n1)
                s2= n2[0:l]
            if d > 0:
                s3= ""
                for i in s2[::-1]:
                    s3+= str( (a[i] + d)%10 )
                    d= (a[i] + d)//10
                if d > 0:
                    s3+= "1"
                s+= s3
            else:
                s+= s2[::-1]
        elif d > 0:
            s+= "1"
        return s[::-1]