class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # n = len(matrix)
        # matrix[:] = [[matrix[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

        # diagonally rotate and then up and down rotate
        n = len(matrix) - 1
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j][n - i] = matrix[n - j][n - i], matrix[i][j]
        for i in range((n + 1) / 2):
            for j in range(n + 1):
                matrix[i][j], matrix[n - i][j] = matrix[n - i][j], matrix[i][j]


