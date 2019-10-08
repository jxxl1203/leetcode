class Solution(object):
    def minWindow(self, s, t):
        table = {}
        for i in t:
            if i in table.keys():
                table[i] += 1
            else:
                table[i] = 0
        l, r = 0, 0
        while r < len(s):



a = Solution()
print a.minWindow("aaaa", "asdasdas")