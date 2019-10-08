class Solution(object):
    def isPalindrome(self, s):
        start = 0
        end = len(s)-1
        s = s.lower()
        import re
        while start < end:
            while start < len(s) and (not re.match("[a-z0-9]", s[start])):
                start += 1
            while end > -1 and (not re.match("[a-z0-9]", s[end])):
                end -= 1
            if start >= end:
                return True
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


a = Solution()
print a.isPalindrome("  12   ad a  1   ")
