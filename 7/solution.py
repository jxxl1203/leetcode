class Solution(object):
    def reverse(self, x):
        if x > 0:
            s = str(x)
        else:
            s = str(x * -1)
            s += "-"
        s = s[::-1]
        res = int(s)
        if res > 0 and res > ((1 << 31) - 1):
            res = 0
        elif res < 0 and res < (-1 << 31):
            res = 0
        return res


solution = Solution()
solution.reverse(-9463847412)
