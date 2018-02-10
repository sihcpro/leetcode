# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        s.split()
        s= [1       if i == 'I' else i for i in s]
        s= [5       if i == 'V' else i for i in s]
        s= [10      if i == 'X' else i for i in s]
        s= [50      if i == 'L' else i for i in s]
        s= [100     if i == 'C' else i for i in s]
        s= [500     if i == 'D' else i for i in s]
        s= [1000    if i == 'M' else i for i in s]
        # print(s)
        summ= s[len(s)-1]
        for i in range(len(s)-2, -1, -1):
            # print(i)
            if s[i+1] > s[i]:
                summ-= s[i]
            else:
                summ+= s[i]
        return summ