# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return 0
        l,r = root.left,root.right
        if l and l.left== None and l.right==None: return l.val+self.sumOfLeftLeaves(r)
        else: return self.sumOfLeftLeaves(l)+self.sumOfLeftLeaves(r)

        