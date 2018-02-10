class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        a= list(s)
        b= [0 for i in range(0,30)]
        for i in a:
            b[ ord(i) - ord('a') ]+= 1
        c= []
        for i in range(0, len(b)):
            if b[i] == 1:
                # print(chr( i+ ord('a') ))
                for j in range(0, len(a)):
                    if a[j] == chr(i+ord('a')):
                        c.append(j)
                        break
        if len(c) > 0:
            return min(c)
        else:
            return -1