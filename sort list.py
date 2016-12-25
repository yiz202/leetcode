

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head is None: return None
        # fast = slow = head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        # slo
        if not head or not head.next: return head
        fast = slow = head
        while fast and fast.next and fast.next.next: slow, fast = slow.next, fast.next.next
        slow.next =  None
        lh, rh = self.sortList(head), self.sortList(fast)
        newH = lh if lh.val < rh.val else rh
        smaller, larger = (lh, rh) if lh.val < rh.val else (rh, lh)
        while smaller and larger:
            while smaller.next and smaller.next.val < larger.val: smaller = smaller.next
            if not smaller.next:
                smaller.next = larger
                break
            tmp = larger.next
            larger.next, smaller.next, larger, smaller = smaller.next, larger, tmp, larger
        return newH
if __name__ == '__main__':
    head = ListNode(1,next=None)
    second = ListNode(-1,next=None)
    head.next = second
    Solution().sortList(head)