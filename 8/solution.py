class Solution(object):
    def myAtoi(self, str):
        i = 0
        f = False
        res = ""
        while i < len(str) and str[i] == " ":
            i += 1
        if i >= len(str):
            return 0
        if str[i] == "+":
            i += 1
        elif str[i] == "-":
            f = True
            i += 1
        elif ord(str[i]) < 48 or ord(str[i]) > 57:
            return 0

        while i < len(str) and str[i] >= "0" and str[i] <= "9":
            res += str[i]
            i += 1
        if len(res) > 0:
            res = int(res)
        else:
            res = 0
        if f:
            res = res * -1
        if res > 0 and res > ((1 << 31) - 1):
            res = 2147483647
        elif res < 0 and res < (-1 << 31):
            res = -2147483648
        return res


s = Solution()
s.myAtoi("   ")



