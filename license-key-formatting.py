class Solution:
    def licenseKeyFormatting(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s= s[::-1].replace("-", "").upper()
        i= 1
        s2= s[0:min(k, len(s)) ]
        while k*i < len(s):
            s2+= "-" + s[k*i:k*(i+1)]
            i+= 1
            # print(s2)
        return s2[::-1]