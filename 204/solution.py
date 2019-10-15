class Solution(object):
    def countPrimes(self, n):
        if n < 2:
            return 0
        primes = [True] * n
        primes[0], primes[1] = False, False
        for i in range(2, int(n**0.5)+1):
            if not primes[i]:
                continue
            j = i * i
            while j < n:
                primes[j] = False
                j += i
        res = 0
        for i in range(2,n):
            if primes[i]:
                res += 1
        return res



a = Solution()
print a.countPrimes(31)
