class Solution(object):
    def myPow(self, x, n):
        def pow(a, b):
            res = 1
            while b:
                if b & 1:
                    res *= a
                b = b >> 1
                a *= a
            return res
        if n == 0:
            return 1
        elif n > 0:
            return pow(x, n)
        else:
            return 1/pow(x, -n)


a = Solution()
print a.myPow(2,10)