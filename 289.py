class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def checkliveNb(i, j):
            live = 0
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [1, 0, -1, 1, -1, 1, 0, -1]
            for k in range(8):
                bx = j + dx[k]
                by = i + dy[k]
                if bx < 0 or bx > m - 1 or by < 0 or by > n - 1:
                    continue
                else:
                    if board[i][j] & 1:
                        live += 1
            return live

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                live = checkliveNb(i, j)
                print live
                if board[i][j] == 0 and live == 3:
                    board[i][j] = 2
                elif board[i][j] == 1:
                    if live < 2 or live > 3:
                        board[i][j] = 1
                    elif live == 2 or live == 3:
                        board[i][j] = 3
                        # for i in range(n):
                        #     for j in range(m):
                        #         board[i][j] >>=1




Solution().gameOfLife([[1,1],[1,0]])