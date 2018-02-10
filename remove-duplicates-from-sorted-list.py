# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, h):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if h is None:
            return None
        n= l= ListNode(h.val)
        while not h is None:
            while not h is None and l.val == h.val:
                h= h.next
            if not h is None:
                l.next= ListNode(h.val)
                l= l.next
        return n
        