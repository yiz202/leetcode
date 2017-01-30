# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def helper(root,stack):
        #     if root is None: return None
        #     helper(root.left,stack)
        #     helper(root.right,stack)
        #     stack.append(root.val)
        # res = []
        # helper(root,res)
        # return res
        if root is None: return []
        stack, list = [], []
        stack.append(root)
        while stack:
            tmp = stack.pop()
            list.append(tmp.val)
            if tmp.left: stack.append(tmp.left)
            if tmp.right: stack.append(tmp.right)
        return list[::-1]


