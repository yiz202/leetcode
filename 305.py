# # Definition for a point.
# # class Point:
# #     def __init__(self, a=0, b=0):
# #         self.x = a
# #         self.y = b
#
# class Solution:
#     # @param {int} n an integer
#     # @param {int} m an integer
#     # @param {Pint[]} operators an array of point
#     # @return {int[]} an integer array
#     def numIslands2(self, n, m, operators):
#         # Write your code here
#         def find(x):
#             p = self.f[x]
#             while p != self.f[p]:
#                     p = self.f[p]
#             while x!= self.f[x]:
#                 next = self.f[x]
#                 self.f[x] = p
#                 x = next
#             return p
#
#         def union(x,y):
#             x = find(x)
#             y = find(y)
#             if x!=y:
#                 self.f[x] = y
#
#         res = []
#         matrix = [[0 for i in range(m)] for j in range(n)]
#         self.f = {}
#         for k, point in enumerate(operators):
#             i = point[0]
#             j = point[1]
#             matrix[i][j] = 1
#             self.f[(i,j)] = (i,j)
#             for x,y  in[(1,0),(-1,0),(0,1),(0,-1)]:
#                 ni,nj = i+x,j+y
#                 if (0< ni < n and 0< nj < m):
#                     if matrix[ni][nj] == 1:
#                         union((i,j),(ni,nj))
#             mapi = {}
#             for points in operators[:k+1]:
#                     points = (points[0],points[1])
#                     find(points)
#             for points in operators[:k+1]:
#                 i = points[0]
#                 j = points[1]
#                 if self.f[(i,j)] not in mapi:
#                     mapi[self.f[(i,j)]] = 1
#                 else:
#                     mapi[self.f[(i,j)]]+=1
#             res.append(len(mapi))
#         return res
#
#
# if __name__ == '__main__':
#     Solution().numIslands2(2, 2, [[0,0],[1,1],[1,0],[0,1]])
#

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    # @param {int} n an integer
    # @param {int} m an integer
    # @param {Pint[]} operators an array of point
    # @return {int[]} an integer array
    def numIslands2(self, n, m, operators):
        # Write your code here
        def find(x):
            p = self.f[x]
            while p != self.f[p]:
                    p = self.f[p]
            while x!= self.f[x]:
                next = self.f[x]
                self.f[x] = p
                x = next
            return p

        def union(x,y):
            x = find(x)
            y = find(y)
            if x!=y:
                self.f[x] = y

        res = []
        matrix = [[0 for i in range(m)] for j in range(n)]
        self.f = {}
        for k, point in enumerate(operators):
            i = point.x
            j = point.y
            matrix[i][j] = 1
            self.f[(i,j)] = (i,j)
            for x,y  in[(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = i+x,j+y
                if (0<= ni < n and 0<= nj < m):
                    if matrix[ni][nj] == 1:
                        union((i,j),(ni,nj))
            mapi = {}
            for points in operators[:k+1]:
                    points = (points.x,points.y)
                    find(points)
            for points in operators[:k+1]:
                i = points.x
                j = points.y
                if self.f[(i,j)] not in mapi:
                    mapi[self.f[(i,j)]] = 1
                else:
                    mapi[self.f[(i,j)]]+=1
            res.append(len(mapi))
        return res





