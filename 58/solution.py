class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        index = s.rfind(" ")
        return max(len(s) - index - 1, 0)


a =Solution()
print a.lengthOfLastWord("hhh hhhhhh  ")

