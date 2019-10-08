class Solution(object):
    def setZeroes(self, matrix):
        n = len(matrix)
        if n == 0:
            return matrix
        m = len(matrix[0])
        first_col = False
        for i in range(n):
            if matrix[i][0] == 0:
                first_col = True
            for j in range(1, m):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, n):
            for j in range(1, m):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        if not matrix[0][0]:
            for i in range(m):
                matrix[0][i] = 0
        if first_col:
            for i in range(n):
                matrix[i][0] = 0
        return matrix


a = Solution()
print a.setZeroes([[1,1,1],[1,0,1],[1,1,1]])