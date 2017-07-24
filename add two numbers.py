# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        tail = dummy
        i = l1
        j = l2
        carry = 0
        while i != None or j != None:
            sum = carry
            sum += i.val if i != None else 0
            sum += j.val if j != None else 0
            carry = sum / 10
            tail.next = ListNode(sum % 10)
            tail = tail.next
            i = i if i is None else i.next
            j = j if j is None else j.next
        if carry:
            tail.next = ListNode(carry)
        return dummy.next


