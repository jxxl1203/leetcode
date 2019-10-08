class Solution(object):
    res = False
    def exist(self, board, word):
        if word == "":
            return True
        n = len(board)
        m = len(board[0])
        used = [[False for i in range(len(board[0]))] for j in range(len(board))]
        self.res = False

        def __dfs(x, y, i):
            if self.res:
                return
            if i == len(word):
                self.res = True
                return
            if ((x - 1 > -1 and used[x - 1][y])
                    and (y - 1 > -1 and used[x][y - 1])
                    and (x + 1 < n and used[x + 1][y])
                    and (y + 1 < m and used[x][y + 1])):
                return
            if x - 1 > -1 and board[x - 1][y] == word[i] and not used[x - 1][y]:
                used[x - 1][y] = True
                __dfs(x - 1, y, i + 1)
                used[x - 1][y] = False
            if y - 1 > -1 and board[x][y - 1] == word[i] and not used[x][y - 1]:
                used[x][y - 1] = True
                __dfs(x, y - 1, i + 1)
                used[x][y - 1] = False
            if x + 1 < n and board[x + 1][y] == word[i] and not used[x + 1][y]:
                used[x + 1][y] = True
                __dfs(x + 1, y, i + 1)
                used[x + 1][y] = False
            if y + 1 < m and board[x][y + 1] == word[i] and not used[x][y + 1]:
                used[x][y + 1] = True
                __dfs(x, y + 1, i + 1)
                used[x][y + 1] = False
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    __dfs(i, j, 1)
                    used[i][j] = False
        return self.res


a = Solution()
print a.exist([["A"]], "B")
