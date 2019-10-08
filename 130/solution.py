class Solution(object):
    def solve(self, board):
        if len(board) < 2:
            return board
        if len(board[0]) < 2:
            return board
        queue = []
        ly = len(board[0]) - 1
        lx = len(board) - 1
        for i in range(len(board)):
            if board[i][0] == 'O':
                board[i][0] = '*'
                queue.append((i, 0))
            if board[i][ly] == 'O':
                board[i][ly] = '*'
                queue.append((i, ly))

        for i in range(1, len(board[0]) - 1):
            if board[0][i] == 'O':
                board[0][i] = '*'
                queue.append((0, i))

            if board[lx][i] == 'O':
                board[lx][i] = '*'
                queue.append((lx, i))

        while queue:
            x, y = queue.pop(0)
            if x > 0:
                if board[x - 1][y] == 'O':
                    board[x - 1][y] = '*'
                    queue.append((x - 1, y))
            if y > 0:
                if board[x][y - 1] == 'O':
                    board[x][y - 1] = '*'
                    queue.append((x, y - 1))
            if x < lx:
                if board[x + 1][y] == 'O':
                    board[x + 1][y] = '*'
                    queue.append((x + 1, y))
            if y < ly:
                if board[x][y + 1] == 'O':
                    board[x][y + 1] = '*'
                    queue.append((x, y + 1))
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == '*':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        return board


a = Solution()
print a.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
