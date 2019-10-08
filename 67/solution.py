class Solution(object):
    def addBinary(self, a, b):
        x = int(a, 2)
        x += int(b, 2)
        return bin(int(str(x), 10))[2:]

a = Solution()
print a.addBinary("1010", "1011")