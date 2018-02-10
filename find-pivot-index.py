class Solution:
    def pivotIndex(self, a):
        """
        :type nums: List[int]
        :rtype: int
        """
        l= [0 for i in a]
        r= [0 for i in a]
        
        for i in range(1, len(a) ):
            l[i]= l[i-1]+a[i-1]
        # print(l)
        for i in range(len(a)-1, 0, -1 ):
            r[i-1]= r[i]+a[i]
        # print(r)
        for i,j in enumerate(l):
            if l[i] == r[i]:
                return i
        return -1
        