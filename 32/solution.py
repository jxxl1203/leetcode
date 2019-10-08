class Solution(object):
    def longestValidParentheses(self, s):
        result = 0
        stack_left = 0
        stack_right = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack_left += 1
            else:
                stack_right += 1
            if stack_right == stack_left:
                result = max(result, stack_right)
            elif stack_right > stack_left:
                stack_left = 0
                stack_right = 0
        stack_left, stack_right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ')':
                stack_right += 1
            else:
                stack_left += 1
            if stack_left == stack_right:
                result = max(result, stack_left)
            elif stack_left > stack_right:
                stack_left = 0
                stack_right = 0
        return result * 2




a = Solution()
print a.longestValidParentheses("))))())()()(()")

"()(()(((())"
"(((())"
"))))())()()(()"