# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 1-2-4-4
# 1-2-4
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        cur = node
        while cur.next:
            cur.val = cur.next.val
            if cur.next.next == None:
                cur.next = None
                break
            cur = cur.next

