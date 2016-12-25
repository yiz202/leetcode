class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        # write your code here
        m = len(board)-1
        n = len(board[0])-1
        visited = [[False]*(n+1) for i in range(m+1)]
        if m == -1 or n == -1: return False
        def dfs(board,i,j,index):
            if i>m or i < 0 or j > n or j < 0 or visited[i][j] or  board[i][j] != word[index]:
                return False

            visited[i][j] = True
            if index == len(word)-1:
                return True
            if dfs(board,i-1,j,index+1) or dfs(board,i+1,j,index+1) or dfs(board,i,j+1,index+1) or dfs(board,i,j-1,index+1) :
                return True
            visited[i][j] = False
            return False

        for i in range(m+1):
            for j in range(n+1):

                    if dfs(board,i,j,0) == True:
                        return True
        return False









