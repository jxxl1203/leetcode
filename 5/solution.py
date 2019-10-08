import time


class Solution(object):
    def longestPalindrome(self, s):
        if len(s) < 2 or s == s[::-1]:
            return s
        start, maxLen = 0, 0
        for i in range(len(s)):
            odd = s[i - maxLen - 1:i + 1]
            even = s[i - maxLen: i + 1]
            if i - maxLen - 1 >= 0 and odd == odd[::-1]:
                start = i - maxLen - 1
                maxLen += 2
            elif i - maxLen >= 0 and even == even[::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start: start + maxLen]

    def longestPalindrome1(self, s):
        if len(s) <= 1:
            return s
        maxLen = 0
        start, end = 0, 0
        for i in range(len(s) - 1):
            l = i
            r = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    start = l
                    end = r
                l -= 1
                r += 1
        for i in range(len(s)):
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if maxLen < r - l + 1:
                    maxLen = r - l + 1
                    start = l
                    end = r
                l -= 1
                r += 1
        return s[start:end + 1]

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_l = 0
        res = ""
        for i in range(0, len(s)):
            left, right = i, i
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
            left, right = i, i + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                if max_l < right - left + 1:
                    max_l = right - left + 1
                    res = s[left:right + 1]
                left -= 1
                right += 1
        return res


# s = " a"
# for i in range(10):
#     s += s
# print len(s)
# sol = Solution()
# t1 = time.time()
# sol.longestPalindrome1("cbbd")
# t2 = time.time()
#
# sol.longestPalindrome2(s)
# t3 = time.time()
#
# print t2 - t1
# print t3 - t2

a = Solution()
print a.longestPalindrome("aaaaabbbbbaaaaaaaaaaaaa")