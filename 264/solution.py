import sys
class Solution(object):
    def __init__(self):
        self.primes = [2,3,5]

    def nthUglyNumber(self, n):
        res = [sys.maxint] * n
        res[0] = 1
        index = [0, 0, 0]
        for i in range(1, n):
            for j in range(3):
                res[i] = min(res[i], self.primes[j] * res[index[j]])
            for j in range(3):
                if res[index[j]] * self.primes[j] == res[i]:
                    index[j] += 1
        return res[-1]


a = Solution()
print a.nthUglyNumber(10)