# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None: return []
        levelNode = [root]
        while levelNode:
            result.append([node.val for node in levelNode])
            new_q = []
            for node in levelNode:
                if node.left: new_q.append(node.left)
                if node.right:new_q.append(node.right)
            levelNode = new_q
        return result[::-1]





