# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         index = [0 for i in range(128)]
#         res = 0
#         start = 0
#         for i, v in enumerate(s):
#             if index[ord(v)] > start:
#                 start = index[ord(s[i])]
#             res = max(res, i - start + 1)
#             index[ord(v)] = i + 1
#         return res


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        his, res, start = {}, 0, 0
        for i, v in enumerate(s):
            if v in his:
                res = max(res, i - start)
                start = max(his[v] + 1, start)
            his[v] = i
        return max(res, len(s) - start)


a = Solution()
print a.lengthOfLongestSubstring("abcacdbbac")