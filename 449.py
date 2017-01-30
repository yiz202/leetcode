# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(node):
            if node:
                res.append(str(node.val))
                helper(node.left)
                helper(node.right)
            else:
                res.append('#')

        res = []
        helper(root)
        return ''.join(res)

        #      def serialize(self, root):
        # def doit(node):
        #     if node:
        #         vals.append(str(node.val))
        #         doit(node.left)
        #         doit(node.right)
        #     else:
        #         vals.append('#')
        # vals = []
        # doit(root)
        # return ' '.join(vals)

    # def deserialize(self, data):
    #     def doit():
    #         val = next(vals)
    #         if val == '#':
    #             return None
    #         node = TreeNode(int(val))
    #         node.left = doit()
    #         node.right = doit()
    #         return node
    #     vals = iter(data.split())
    #     return doit()


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def helper():
            nodestr = next(li)
            if nodestr == '#':
                return None
            else:
                node = TreeNode(int(nodestr))
                node.left = helper()
                node.right = helper()
                return node

        li = iter(data.split())
        return helper()
        # Your Codec object will be instantiated and called as such:
        # codec = Codec()
        # codec.deserialize(codec.serialize(root))