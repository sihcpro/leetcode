class Solution:
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s2= ""
        i= 0
        n= len(s)
        while i < n:
            s3= ""
            for j in range(0, min( k, n-i)):
                s3+= s[i]
                i+= 1
            s2+= s3[::-1]
            # print(s2)
            while i < n and i % (2*k) != 0:
                s2+= s[i]
                i+= 1
            # print("="+s2)
        return s2