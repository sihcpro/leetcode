class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a= [ -1 for i in nums1]
        b= [ -1 for i in range(0,10005)]
        c= []
        for i in range(len(nums2)-1, -1, -1):
            sp= nums2[i]
            while len(c) != 0 and c[len(c)-1] < sp:
                c.pop()
            if len(c) != 0:
                b[ sp ]= c[len(c)-1]
            c.append(sp)
        for i in range(0,len(nums1)):
            a[i]= b[ nums1[i] ]
        return a
        