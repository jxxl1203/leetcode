class Solution(object):
    def intToRoman(self, num):
        result = ""
        if 0 < num / 1000 < 4:
            result += "M" * (num / 1000)

        num = num - 1000 * (num / 1000)
        if 0 < num / 100 < 4:
            result += "C" * (num / 100)
        elif num / 100 == 4:
            result += "CD"
        elif 4 < num / 100 < 9:
            result += "D"
            result += "C" * (num / 100 - 5)
        elif num / 100 == 9:
            result += "CM"

        num = num - 100 * (num / 100)
        if 0 < num / 10 < 4:
            result += "X" * (num / 10)
        elif num / 10 == 4:
            result += "XL"
        elif 4 < num / 10 < 9:
            result += "L"
            result += "X" * (num / 10 - 5)
        elif num / 10 == 9:
            result += "XC"

        num = num - 10 * (num / 10)
        if 0 < num < 4:
            result += "I" * num
        elif num == 4:
            result += "IV"
        elif 4 < num < 9:
            result += "V"
            result += "I" * (num - 5)
        elif num == 9:
            result += "IX"
        return result


a = Solution()
print a.intToRoman(600)