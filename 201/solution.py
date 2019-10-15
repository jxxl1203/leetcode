class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        if m == 0:
            return 0
        count = 0
        while m != n:
            m >>= 1
            n >>= 1
            count += 1
        return n << count


