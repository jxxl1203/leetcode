class Solution(object):
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
        table = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        i, j = 0, 0
        width = len(matrix[0])
        height = len(matrix)
        direction = 0
        res = []
        while len(res) < (height * width):
            res.append(matrix[i][j])
            table[i][j] = True
            if direction == 0:
                j += 1
                if j >= width or table[i][j]:
                    j -= 1
                    direction = 1
                    i += 1
            elif direction == 1:
                i += 1
                if i >= height or table[i][j]:
                    i -= 1
                    direction = 2
                    j -= 1
            elif direction == 2:
                j -= 1
                if j < 0 or table[i][j]:
                    j += 1
                    direction = 3
                    i -= 1
            else:
                i -= 1
                if i < 0 or table[i][j]:
                    j += 1
                    i += 1
                    direction = 0
        return res


a = Solution()
print a.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])