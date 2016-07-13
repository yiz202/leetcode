# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        result = self.dfs(root,[],1)
        return min(result) if result is not None else 1


    def dfs(self,root,result,num):
        if root.left is None and root.right is None:
            result.append(num)
            num-=1
            return
        if root.left: self.dfs(root.left,result,num+1)
        if root.right:self.dfs(root.right,result,num+1)
        num-=1
        return result
        