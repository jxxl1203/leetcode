class Solution(object):
    def strStr(self, haystack, needle):
        l = len(needle)
        next = [0] * l
        j = 1
        k = 0
        while j < l:
            while k > 0 and needle[j] != needle[k]:
                k = next[k-1]
            if needle[j] == needle[k]:
                k += 1
            next[j] = k
            j += 1
        i = 0
        while i <= len(haystack) - l:
            j = 0
            flag = True
            while j < l:
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    i += next[j]
                    flag = False
                    break
            if flag:
                return i
            i += 1
        return -1



a = Solution()
print a.strStr("aaaaa", "bba")
#

# st = ""
# for i in range(2):
#     split = str(uuid.uuid4()).split("-")
#     s = "".join(split)
#     st += s



"mississippi"
"issip"

"aaaaa"
"bba"