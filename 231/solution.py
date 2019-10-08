class Solution(object):
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False
        return n & n-1 == 0


a = Solution()
print a.isPowerOfTwo(1023)