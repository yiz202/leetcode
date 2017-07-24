# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def sortHelper(start, end):
            if start > end: return None
            mid = (start + end) / 2
            root = TreeNode(nums[mid])
            root.left = sortHelper(start, mid - 1)
            root.right = sortHelper(mid + 1, end)
            return root

        return sortHelper(0, len(nums) - 1)

