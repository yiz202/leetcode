class Solution:
    """
    @param matrix: A list of lists of integers
    @return: Nothing
    """

    def rotate(self, matrix):
        # write your code here
        n = len(matrix)
        for i in range(n / 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
