class Solution(object):
    def romanToInt(self, s):
        result = 0
        i = 0
        table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < len(s):
            if (i+1) < len(s) and table[s[i]] < table[s[i+1]]:
                result += table[s[i+1]] - table[s[i]]
                i += 2
            else:
                result += table[s[i]]
                i += 1
        return result


a = Solution()
print a.romanToInt("MCMXCIV")
