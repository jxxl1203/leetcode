class Solution(object):
    def climbStairs(self, n):
        n += 1
        return int(1/5 ** 0.5 * (pow((1 + 5 ** 0.5) / 2, n) - pow((1 - 5 ** 0.5) / 2, n)))


a = Solution()
print a.climbStairs(6)