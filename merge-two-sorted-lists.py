# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        n= l= ListNode(0)
        if l2 is None or ( not l1 is None and l1.val < l2.val ):
            l.val= l1.val
            l1= l1.next
        else:
            l.val= l2.val
            l2= l2.next
        while not l1 is None or not l2 is None:
            l.next= ListNode(0)
            l= l.next
            if l2 is None or ( not l1 is None and l1.val < l2.val ):
                l.val= l1.val
                l1= l1.next
            else:
                l.val= l2.val
                l2= l2.next
            
        return n
        