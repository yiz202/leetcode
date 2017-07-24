class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        def settozeroRow(rowi,coli,matrix):
            for col in range(len(matrix[rowi])):
                matrix[rowi][col] = 0
        def settozeroCol(rowi,coli,matrix):
            for row in range(len(matrix)):
                matrix[row][coli] = 0
        seenCol = set()
        seenRow = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0 and n not in seenRow:
                    settozeroRow(i,j,matrix)
                if matrix[i][j]==0 and m not in seenCol:
                    settozeroCol(i,j,matrix)
                seenCol.add(j)
                seenRow.add(i)






Solution().setZeroes([[0,1],[1,1]])