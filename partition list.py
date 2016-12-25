

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        dummy = ListNode(0)
        l2 = ListNode(0)
        dummy.next = head
        head1 = dummy
        head2 = l2
        while dummy and dummy.next:
            if dummy.next.val >= x:
                l2.next = dummy.next
                dummy.next = dummy.next.next
                l2 = l2.next
            else:
                dummy = dummy.next
        dummy.next = head2.next
        return head1.next
Solution().partition(1->4->3->2->5->2->null, 3)