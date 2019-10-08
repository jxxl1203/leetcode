class Solution(object):
    def countAndSay(self, n):
        s = "1"
        tmp = ""
        repeat = 1
        for deep in range(1,n):
            for i in range(len(s)):
                if i + 1 < len(s) and s[i] == s[i + 1]:
                    repeat += 1
                    continue
                tmp += str(repeat) + s[i]
                repeat = 1
            s = tmp
            tmp = ""
        return s

a = Solution()
print a.countAndSay(2)