# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        def helper(root, sum, target):
            sum += root.val
            if root.left is None and root.right is None and sum == target:
                return True
            elif root.left is None and root.right is None and sum != target:
                return False
            res = False
            if root.left:
                res = res or helper(root.left, sum, target)
            if root.right:
                res = res or helper(root.right, sum, target)
            return res

        if root == None: return False
        return helper(root, 0, sum)





        # def helper(node,sum,q,stack):
        #     if not node: return
        #     sum -= node.val
        #     q.append(node.val)

        #     if not node.left and not node.right:
        #         if sum == 0:
        #             stack.append(q)
        #     else:
        #         helper(node.left,sum,q,stack)
        #         helper(node.right,sum,q,stack)
        #     q.pop()
        # stack = []
        # if not root: return []
        # helper(root,sum,[],stack)
        # return stack