# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a= []
        h= head
        while not h is None:
            a.append(h.val)
            h= h.next
        a.reverse()
        h= head
        for i in a:
            h.val= i
            h= h.next
        return head
        
        