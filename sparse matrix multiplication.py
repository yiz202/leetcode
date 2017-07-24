class Solution:
    # @param {int[][]} A a sparse matrix
    # @param {int[][]} B a sparse matrix
    # @return {int[][]} the result of A * B
    def multiply(self, A, B):
        # Write your code here
        matrix = [[0 for i in range(len(B[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(A[0])):
                    if A[i][k] == 0 or B[k][j] == 0:
                        continue
                    else:
                        matrix[i][j] += A[i][k] * B[k][j]
        return matrix

