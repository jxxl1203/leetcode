class Solution(object):
    def rotate(self, matrix):
        l = len(matrix)
        for i in range(l / 2):
            for j in range(i, l - i - 1):
                matrix[i][j], matrix[j][l - i - 1], matrix[l - i - 1][l - j - 1], matrix[l - j - 1][i] = matrix[l - j - 1][i], matrix[i][j], matrix[j][l - i - 1], matrix[l - i - 1][l - j - 1]
        return matrix


a = Solution()
li = a.rotate([[1,2],[3,4]])

for l in li:
    print l