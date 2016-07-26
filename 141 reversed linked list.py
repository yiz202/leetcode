# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        curr1 = curr2 = head
        while curr2 and curr2.next:
            curr1 = curr1.next
            curr2 = curr2.next.next
            if curr2 == curr1: return True
        return False