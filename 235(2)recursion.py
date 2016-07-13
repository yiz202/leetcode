# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # # if root is None: return root
        # if p.val < root.val and q.val < root.val: self.lowestCommonAncestor( root.left, p, q)
        # elif p.val > root.val and q.val > root.val: self.lowestCommonAncestor( root.right, p, q)
        # elif p.val<= root.val and q.val >=root.val or p.val>= root.val and q.val<=root.val:
        #     return root
        # if p.val < root.val and q.val < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # elif p.val > root.val and q.val > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # else:
        #     return root
        if p.val < root.val and q.val < root.val: return self.lowestCommonAncestor( root.left, p, q)
        elif p.val > root.val and q.val > root.val: return self.lowestCommonAncestor( root.right, p, q)
        elif p.val<= root.val and q.val >=root.val or p.val>= root.val and q.val<=root.val:
            return root
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    Solution().lowestCommonAncestor(root,root.left.left.left,root.left.right)