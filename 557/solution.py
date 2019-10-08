# class Solution(object):
#     def reverseWords(self, s):
#         if s == "":
#             return s
#         arr = []
#         for i in s:
#             arr.append(i)
#         arr.reverse()
#         s = "".join(arr)
#         arr = s.split(" ")
#         arr.reverse()
#         return " ".join(arr)
class Solution:
    def reverseWords(self, s):
        return " ".join([i[::-1] for i in s.split()])


a = Solution()
print a.reverseWords("Let's take LeetCode contest")