import math
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x < 10:
            return True
        i = 1
        j = 0
        tmp = x
        p = 0
        while x / i >= 10:
            i *= 10

        while tmp > 0:
            p += tmp % 10 * i + (tmp / i) * math.pow(10, j)
            tmp = (tmp - (tmp / i) * i - tmp % 10) / 10
            j += 1
            i = i / 10
        return int(p) == x

s = Solution()
s.isPalindrome(33)