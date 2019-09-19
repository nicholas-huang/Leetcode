# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        h = head
        while h:
            
            tmp = h.next
            if tmp is None:
                break
            while tmp and tmp.val == h.val:
                h.next = tmp.next
                tmp.next = None
                tmp = h.next
            h = h.next
        return head