class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        index = 0
        flag = False
        while len(strs) > 0:
            if index >= len(strs[0]):
                break
            for i in range(len(strs) - 1):
                if index >= len(strs[i]) or index >= len(strs[i + 1]) or strs[i][index] != strs[i + 1][index]:
                    flag = True
                    break
            if flag:
                break
            index += 1
        return strs[0][:index]


a = Solution()
print a.longestCommonPrefix(["aa","a"])
print a.longestCommonPrefix(["dog","racecar","car"])
print a.longestCommonPrefix(["flower","flow","floght"])