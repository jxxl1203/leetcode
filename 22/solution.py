class Solution(object):
    result = []
    def generateParenthesis(self, n):
        self.generate(n, 0, 0, "")
        return self.result

    def generate(self, n, l, r, s):
        if l == r and n == r:
            self.result.append(s)
            return
        if l == r:
            self.generate(n, l + 1, r, s + "(")
        else:
            if l < n:
                self.generate(n, l + 1, r, s + "(")
            if r < n:
                self.generate( n, l, r + 1, s + ")")



a = Solution()
print a.generateParenthesis(1)