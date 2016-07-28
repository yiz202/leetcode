# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A,B = 0,0
        currA  = headA
        currB = headB
        while currA and currB:
            if currA is currB: return currA
            if currA.next == None and A == 0:
                currA = headB
                A =1
            else: currA = currA.next
            if currB.next == None and B == 0:
                currB = headA
                B=1
            else:
                currB = currB.next
        return None


if __name__ == '__main__':
    headA = ListNode(1)
    headB = ListNode(5)
    c = ListNode(3)

    d = ListNode(4)
    c.next = d
    headA.next = c

    Solution().getIntersectionNode(headA,headB)
