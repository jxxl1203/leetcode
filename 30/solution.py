class Solution(object):
    def findSubstring(self, s, words):
        if len(words) == 0:
            return []
        word_map = {}
        used_map = {}
        word_len = len(words[0])
        result = []
        total_len = word_len * len(words)
        i = 0
        for str in words:
            if str in word_map:
                word_map[str] += 1
            else:
                word_map[str] = 1
        while i <= len(s) - total_len:
            for j in range(word_len):
                flag = True
                for k in range(len(words)):
                    tmp = s[i+j+k*word_len:i+j+(k+1)*word_len]
                    if tmp in word_map:
                        if tmp in used_map:
                            if used_map[tmp] < word_map[tmp]:
                                used_map[tmp] += 1
                            else:
                                flag = False
                                break
                        else:
                            used_map[tmp] = 1
                    else:
                        flag = False
                        break
                if flag:
                    result.append(i+j)
                used_map = {}
            i += word_len

        return result


a = Solution()
result = a.findSubstring("", [])
print result