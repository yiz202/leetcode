# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
1234
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next =head
        curr = dummy
        while curr.next and curr.next.next:
            after = curr.next.next
            before = curr.next
            newCur = after.next
            curr.next = after
            curr.next.next = before
            before.next = newCur
            curr = curr.next.next
        return dummy.next
