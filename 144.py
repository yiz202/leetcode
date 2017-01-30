# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def helper(root,stack):
        #     if root is None: return None
        #     stack.append(root.val)
        #     helper(root.left,stack)
        #     helper(root.right,stack)
        # res = []
        # helper(root,res)
        # return res
        stack = []
        arr = []
        if root is None: return stack
        stack.append(root)
        while stack:
            tmp = stack.pop()
            arr.append(tmp.val)
            if tmp.right:
                stack.append(tmp.right)
            if tmp.left:
                stack.append(tmp.left)
        return arr



