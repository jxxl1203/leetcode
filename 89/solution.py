class Solution(object):
    def grayCode(self, n):
        res = []
        for i in range(0, 1 << n):
            res.append(i ^ i >> 1)
        return res


a = Solution()
print a.grayCode(5)