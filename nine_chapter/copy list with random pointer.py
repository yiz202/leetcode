# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        # write your code here
        if head is None: return None
        cur = head
        while cur:
            nextoldcur = cur.next
            cur.next = RandomListNode(cur.label)
            cur.next.next = nextoldcur
            cur = cur.next.next
        cur = head
        while cur and cur.next:
            if cur.random is not None:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        # print '0'
        cur = head.next
        # print 'f'
        while cur and cur.next:
            # print cur.label

            tmp = cur.next.next
            cur.next = tmp
            cur = cur.next



        return head.next
