class Solution(object):
    def solveNQueens(self, n):
        res = []
        chess_board = [[0 for i in range(n)] for j in range(n)]

        def nQueue(board, d):
            n = len(board)
            if d == n:
                s_board = []
                for i in range(n):
                    s = ""
                    for j in range(n):
                        if board[i][j] < 0:
                            s += "Q"
                        else:
                            s += "."
                    s_board.append(s)

                res.append(s_board)
                return
            for i in range(n):
                if board[d][i] == 0:
                    board[d][i] = -n
                    f = 1
                    while (d - f > -1) or (d + f < n) or (i - f > -1) or (i + f < n):
                        if d - f > -1:
                            board[d - f][i] += 1
                            if i - f > -1:
                                board[d][i - f] += 1
                            if i + f < n:
                                board[d][i + f] += 1
                        if d + f < n:
                            board[d + f][i] += 1
                            if i - f > -1:
                                board[d + f][i - f] += 1
                            if i + f < n:
                                board[d + f][i + f] += 1
                        if i - f > -1:
                            board[d][i - f] += 1
                        if i + f < n:
                            board[d][i + f] += 1

                        f += 1

                    nQueue(board, d+1)
                    f = 1
                    while (d - f > -1) or (d + f < n) or (i - f > -1) or (i + f < n):
                        if d - f > -1:
                            board[d - f][i] -= 1
                            if i - f > -1:
                                board[d][i - f] -= 1
                            if i + f < n:
                                board[d][i + f] -= 1
                        if d + f < n:
                            board[d + f][i] -= 1
                            if i - f > -1:
                                board[d + f][i - f] -= 1
                            if i + f < n:
                                board[d + f][i + f] -= 1
                        if i - f > -1:
                            board[d][i - f] -= 1
                        if i + f < n:
                            board[d][i + f] -= 1
                        f += 1

                    board[d][i] = 0
            return
        nQueue(chess_board, 0)
        return res




a =Solution()
arr = a.solveNQueens(4)

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print arr[i][j]
    print