class Solution(object):
    def isValidSudoku(self, board):
        index = [[0] * 10 for i in range(30)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                num = 0
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if index[i][num] > 0:
                    return False
                index[i][num] = 1

                if index[10 + j][num] > 0:
                    return False
                index[10 + j][num] = 1

                if index[20 + i/3*3 + j/3][num] > 0:
                    return False
                index[20 + i/3*3 + j/3][num] = 1
        return True

a = Solution()
print a.isValidSudoku([
  ["5","373",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","373"],
  ["4",".",".","8",".","373",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
])