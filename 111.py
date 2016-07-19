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


# BFS solution
    # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution(object):
#     def minDepth(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         if root is None: return 0
#         i,levelNode = 1,[root]
#         result = []
#         while levelNode:
#             new_q = []
#             for node in levelNode:
#                 if node.left: new_q.append(node.left)
#                 if node.right:new_q.append(node.right)
#                 if node.left is None and node.right is None: return i
#             levelNode = new_q
#             i+=1
#
