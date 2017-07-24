class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        k = 0
        matrix = [[0 for i in range(n)] for j in range(n)]
        rowbegin = 0
        rowend = n - 1
        colbegin = 0
        colend = n - 1
        while colbegin <= colend and rowbegin <= rowend:
            for i in range(colbegin, colend + 1):
                k += 1
                matrix[rowbegin][i] = k
            rowbegin += 1
            for i in range(rowbegin, rowend + 1):
                k += 1
                matrix[i][colend] = k
            colend -= 1

            for i in range(colend, colbegin - 1, -1):
                k += 1
                matrix[rowend][i] = k
            rowend -= 1
            for i in range(rowend, rowbegin - 1, -1):
                k += 1
                matrix[i][colbegin] = k
            colbegin += 1
            print matrix
        return matrix