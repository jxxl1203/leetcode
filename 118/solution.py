class Solution(object):
    def generate(self, numRows):
        res = []
        for i in range(numRows):
            tmp = [1] * (i + 1)
            for j in range(i):
                if i-1 > - 1 and j - 1 > -1 and j < i:
                    tmp[j] = res[i-1][j-1] + res[i-1][j]
            res.append(tmp)
        return res



a = Solution()
print a.generate(5)