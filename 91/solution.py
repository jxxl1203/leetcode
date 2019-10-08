class Solution(object):
    def numDecodings(self, s):
        if len(s) == 0 or (s == '0'):
            return 0
        if len(s) == 1:
            return 1
        res = [0 for i in range(len(s)+1)]
        res[0] = 1
        for i in range(0, len(s)):
            if s[i] == '0':
                res[i+1] = 0
            else:
                res[i+1] = res[i]
            if s[i-1] == '1' or (s[i-1] == '2' and s[i] <= '6'):
                res[i+1] += res[i-1]
        print res
        return res[-1]



a = Solution()
print a.numDecodings('226')

