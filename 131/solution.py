class Solution(object):
    def partition(self, s):
        self.res = []
        def _helper(s, list):
            if s == "":
                self.res.append(list)
                return
            for i in range(0,len(s)):
                tmp = s[:i+1]
                if is_palindrome(tmp):
                    _helper(s[i+1:], list + [tmp])


        def is_palindrome(s):
            l = len(s)-1
            for i in range(l/2+1):
                if s[i] != s[l-i]:
                    return False
            return True

        _helper(s, [])

        return self.res


a = Solution()
print a.partition("aab")
