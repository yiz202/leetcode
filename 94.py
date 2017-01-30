# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def helper(root,stack):
        #     if root is None: return None
        #     if root.left:
        #         helper(root.left,stack)
        #     stack.append(root.val)
        #     if root.right:
        #         helper(root.right,stack)
        # res = []
        # helper(root,res)
        # return res
        if root is None: return []
        lis = []
        stack = []
        cur = root
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            tmp = stack.pop()
            lis.append(tmp.val)
            cur = tmp.right




