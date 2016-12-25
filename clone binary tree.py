"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """
    def cloneTree(self, root):
        # Write your code here
        if root is None: return None
        tn = TreeNode(root.val)
        self.help(root,tn)

    def help(self,root,tn):
        if root == None: return None
        if root.left:
            tl = TreeNode(root.left.val)
            tl = tn.left
            self.help(root.left,tl)

        if root.right:
            tr = TreeNode(root.right.val)
            tr = tn.right
            self.help(root.right,tr)

        return tn





