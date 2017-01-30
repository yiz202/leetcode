# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNodeeeeeeeef
        :type sum: int
        :rtype: int
        """

        def subpath(node, sum):
            if not node: return 0
            subres = (node.val == sum)
            subres += subpath(node.left, sum - node.val)
            subres += subpath(node.right, sum - node.val)
            return subres

        if not root: return 0
        ans = subpath(root, sum)
        ans += self.pathSum(root.left, sum)
        ans += self.pathSum(root.right, sum)
        return ans


