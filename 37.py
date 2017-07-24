class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def solve(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in range(1, 10):
                            if check(board, i, j, str(k)):
                                board[i][j] = str(k)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = '.'
                                    return False

        def check(board, i, j, val):
            for c in range(9):
                if board[i][c] == val or board[c][j] == val: return False
                if board[3 * (i / 3) + i / 3][3 * (j / 3) + j % 3] == val: return False
            return True

        if not board or len(board) != 9 or len(board[0]) != 9: return
        solve(board)






Solution().solveSudoku(["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."])