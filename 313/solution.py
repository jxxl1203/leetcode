import sys

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        res = [sys.maxint] * n
        res[0] = 1
        index = [0] * len(primes)
        for i in range(1, n):
            for j in range(len(index)):
                res[i] = min(res[i], primes[j] * res[index[j]])
            for j in range(len(index)):
                if res[i] / res[index[j]] == primes[j]:
                    index[j] += 1
        return res[-1]

a = Solution()
print a.nthSuperUglyNumber(12, [2, 7, 13, 19])
