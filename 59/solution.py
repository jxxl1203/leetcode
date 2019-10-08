class Solution(object):
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for j in range(n)]
        left, right, top, button, val = 0, n, 0, n, 0
        while val < n*n:
            for i in range(left, right):
                val += 1
                res[top][i] = val
            top += 1
            for i in range(top, button):
                val += 1
                res[i][right-1] = val
            right -= 1
            for i in range(right - 1, left - 1, -1):
                val += 1
                res[button-1][i] = val
            button -= 1
            for i in range(button - 1, top - 1, -1):
                val += 1
                res[i][left] = val
            left += 1
        return res


a = Solution()

print a.generateMatrix(1)
