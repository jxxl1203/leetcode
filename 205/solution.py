# class Solution(object):
#     def isIsomorphic(self, s, t):
#         if len(s) != len(t):
#             return False
#         mapping = {}
#         his = set()
#         for i in range(len(s)):
#             if mapping.has_key(s[i]):
#                 if mapping[s[i]] != t[i]:
#                     return False
#             elif t[i] in his:
#                 return False
#             mapping[s[i]] = t[i]
#             his.add(t[i])
#         return True

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        map1 = {}
        map2 = {}
        for i, j in zip(s, t):
            if i in map1:
                if map1[i] != j:
                    return False
            else:
                if j in map2:
                    return False
                map1[i] = j
                map2[j] = i
        return True

a = Solution()
print a.isIsomorphic("bbcc", "aadd")