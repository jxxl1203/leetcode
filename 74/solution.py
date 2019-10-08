class Solution(object):
    def searchMatrix(self, matrix, target):
        n = len(matrix)
        if n == 0:
            return False
        m = len(matrix[0])
        if m == 0:
            return False
        l = 0
        r = n * m - 1
        while l <= r:
            mid = (l + r) / 2
            x = mid / m
            y = mid % m
            if matrix[x][y] < target:
                l = mid + 1
            elif matrix[x][y] > target:
                r = mid - 1
            else:
                return True
        return False



a = Solution()
print a.searchMatrix([[1],[3]], 1)
