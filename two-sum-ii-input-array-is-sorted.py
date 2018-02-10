class Solution:
    def twoSum(self, a, k):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i= 0
        j= len(a)-1
        while i < j:
            if a[i] + a[j] == k:
                return [i+1, j+1]
            elif a[i] + a[j] < k:
                i+=1
            else:
                j-=1