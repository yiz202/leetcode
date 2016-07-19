# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution:
#     # @param {TreeNode} root
#     # @return {string[]}
#     def binaryTreePaths(self, root):
#         if root is None: return []
#         return self.dfs(root,[str(root.val)],[])
#
#     def dfs(self,currNode,tmpstr,li):
#         if not currNode.left and not currNode.right:
#             li.append(''.join(tmpstr))
#             tmpstr.pop()
#             return
#         if currNode.left:
#             tmpstr.append("->")
#             tmpstr.append( str(currNode.left.val))
#             self.dfs(currNode.left,tmpstr,li)
#
#             # tmpstr.pop()
#         if currNode.right:
#             tmpstr.append("->")
#             tmpstr.append( str(currNode.right.val))
#             self.dfs(currNode.right,tmpstr,li)
#         tmpstr.pop()
#         return li
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        result = []
        if root is None:
            return result
        self.dfs(root, result, [])
        return result

    def dfs(self, node, result, tmp):
        tmp.append(str(node.val))
        if node.left is None and node.right is None:
            result.append('->'.join(tmp))
            tmp.pop()
            return

        if node.left:
            self.dfs(node.left, result, tmp)
        if node.right:
            self.dfs(node.right, result, tmp)
        tmp.pop()




# dfs sulution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# class Solution:
#     # @param {TreeNode} root
#     # @return {string[]}
#     def binaryTreePaths(self, root):
#         result = []
#         if root is None: return []
#         def dfs(node,path):
#             if node.left is None and node.right is None: result.append(path)
#             if node.left: dfs(node.left,path+"->" + str(node.left.val))
#             if node.right: dfs(node.right,path+"->"+str(node.right.val))
#         dfs(root,str(root.val))
#         return result





if __name__ == '__main__':
    root = TreeNode(1)
    # root.left = TreeNode(2)
    #
    # root.right = TreeNode(3)
    #
    # root.left.left = TreeNode(5)
    # root.left.left.left = TreeNode(6)


    Solution().binaryTreePaths(root)