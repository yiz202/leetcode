class Solution:
    def spiralMatrix(self,matrix):
        m = len(matrix)
        n = len(matrix[0])
        down = (-1,0)
        up = (1,0)
        left = (0,-1)
        right = (0,1)
        i,j = 0,0
        tmpi, tmpj = -1,-1
        for j in range(n):
            print matrix[i][j]
            if j == n-1:
                for x,y in down:
                    i +=x
                    j+=y
                    break

        for i in range(m):
            print matrix[i][j]
            if i == m-1:
                for x,y in left:
                    i+=x
                    j+=y
        for j in range(n-1,tmpj,-1):
            print matrix[i][j]
            if j == tmpj+1:
                for x, y in 


