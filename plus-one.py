class Solution:
    def plusOne(self, a):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a= a[::-1]
        for i in range(len(a)):
            if a[i] == 9:
                a[i]= 0
            else:
                a[i]+= 1
                return a[::-1]
        a.append(1)
        return a[::-1]