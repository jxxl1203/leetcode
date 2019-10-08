class Solution(object):
    # def convert(self, s, numRows):
    #     if numRows == 1:
    #         return s
    #     t = 2 * (numRows - 1)
    #     res = ""
    #     for i in range(numRows):
    #         j = 0
    #         while 1:
    #             if t * j + i >= len(s):
    #                 break
    #             res += s[t * j + i]
    #             if i % (numRows - 1) != 0 and t * (j+1) - i < len(s):
    #                 res += s[t * (j+1) - i]
    #             j += 1
    #     return res
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        t = 2 * (numRows - 1)
        arr = [""] * numRows
        res = ""
        for i in range(len(s)):
            if i % t < numRows:
                arr[i % t] += s[i]
            else:
                arr[t - i % t] += s[i]
        for i in arr:
            res += i
        return res

solu = Solution()
print solu.convert("PAYPALISHIRING", 4)
