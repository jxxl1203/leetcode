class Solution(object):
    def divide(self, dividend, divisor):
        bit = 1
        result = 0
        divid = abs(dividend)
        divis = abs(divisor)
        while divid >= divis << 1:
            divis <<= 1
            bit <<= 1
        while bit > 0 and divid > 0:
            if divid >= divis:
                divid -= divis
                result += bit

            divis >>= 1
            bit >>= 1
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            result = -result

        return min(result, (1 << 31) - 1)


a = Solution()
print a.divide(1024, 1)