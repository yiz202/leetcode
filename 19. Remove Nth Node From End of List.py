# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        slow =fast = dummy
        dummy.next = head
        for i in range(n):
            slow = slow.next
        while slow.next is not None:
            fast = fast.next
            slow = slow.next
        fast.next = fast.next.next
        return dummy.next

        