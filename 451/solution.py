import copy
class Solution(object):
    def frequencySort(self, s):
        res = ""
        table = [0] * 127
        for i in s:
            table[ord(i)] += 1
        table1 = copy.deepcopy(table)
        table.sort()
        for i in range(126, -1, -1):
            if table[i] == 0:
                break
            for j in range(0, 127):
                if table1[j] == table[i]:
                    res += chr(j) * table1[j]
                    table1[j] = 0
        return res


a = Solution()
print a.frequencySort("112233aaabbbb  ")


m = {"1":3, "2":2, "373":1}
print m.items()
print sorted(m.items(), key=lambda x : x[0])
print sorted(m.items(), key=lambda x : x[1])