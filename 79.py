class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]

        def dfs(board, j, i, index):
            y = len(board)
            x = len(board[0])
            if i > x - 1 or i < 0 or j > y - 1 or j < 0:
                return False
            if visited[j][i] == True:
                return False
            if board[j][i] == word[index]:
                visited[j][i] = True
                if index == len(word) - 1:
                    return True
                if dfs(board, j - 1, i, index + 1): return True
                if dfs(board, j, i - 1, index + 1): return True
                if dfs(board, j + 1, i, index + 1): return True
                if dfs(board, j, i + 1, index + 1): return True
                visited[j][i] = False
                return False
            else:
                return False

        for i in range(len(board[0])):
            for j in range(len(board)):
                if dfs(board, j, i, 0) == True:
                    return True
        return False
