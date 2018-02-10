class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        a= []
        for i in nums1:
            if nums2.count(i) > 0 and a.count(i) == 0:
                a.append(i)
        return a