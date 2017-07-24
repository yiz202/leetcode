# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # def traverse(node):
        #     if not node: return
        #     ds[node.val]+=1
        #     traverse(node.left)
        #     traverse(node.right)
        # if not root: return []
        # ds = collections.defaultdict(int)
        # traverse(root)
        # res = []
        # tupleRes = sorted(ds.items(),key=lambda x:x[1],reverse = True)
        # print tupleRes
        # mode = tupleRes[0][1]
        # for t in tupleRes:
        #     if t[1] == mode:
        #         res.append(t[0])
        # return res


        def inorder(node):
            curNode = node
            pre = None
            res = []
            stack = []
            count = 1
            maxKeep = 1
            while curNode or stack:
                while curNode:
                    stack.append(curNode)
                    curNode = curNode.left
                tmp = stack.pop()
                if pre:
                    if pre.val == tmp.val:
                        count += 1
                    else:
                        count = 1
                if count >= maxKeep:
                    if count > maxKeep: res[:] = []
                    res.append(tmp.val)
                    maxKeep = count
                if not pre:
                    pre = TreeNode(tmp.val)
                else:
                    pre.val = tmp.val
                curNode = tmp.right
            return res

        return inorder(root)







