class Solution(object):
    def uniquePaths(self, m, n):
        if n > m:
            n, m = m, n
        res = [1] * m
        for i in range(n - 1):
            for j in range(1, m):
                res[j] += res[j-1]
        return res[-1]


a = Solution()
print a.uniquePaths(0,0)