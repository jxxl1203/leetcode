class Solution(object):
    def getRow(self, rowIndex):
        if rowIndex == 0:
            return [1]
        res = [1] * (rowIndex+1)
        for i in range(rowIndex):
            for j in range(i, 0, -1):
                res[j] += res[j-1]
        return res


a = Solution()
print a.getRow(1)