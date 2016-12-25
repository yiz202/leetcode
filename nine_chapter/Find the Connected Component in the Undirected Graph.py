# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    # @return {int[][]} a connected set of a undirected graph

    def dfs(self,x,tmp):
        self.v[x.label] = True
        tmp.append(x.label)
        for n in x.neighbors:
            if not self.v[n.label]:
                self.dfs(n,tmp)

    def connectedSet(self, nodes):
        # Write your code here
        self.v = {}
        res = []

        for n in nodes:
            self.v[n.label] = False
        for n in nodes:
            if self.v[n.label] == False:
                tmp = []
                self.dfs(n,tmp)
                res.append(sorted(tmp))
        return res

    