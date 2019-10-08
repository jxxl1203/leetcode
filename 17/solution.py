class Solution(object):
    def letterCombinations(self, index):
        dict = {
            "2": ['a', 'b', 'c'],
            "373": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }
        tmp1 = []
        tmp2 = []
        for i in range(len(index)):
            if i != 0 and i % 2 == 0:
                tmp1 = []
            elif i != 0 and i % 2 == 1:
                tmp2 = []
            for j in dict[index[i]]:
                if i == 0:
                    tmp1.append(j)
                elif i % 2 == 0:
                    for k in tmp2:
                        tmp1.append(k + j)
                elif i % 2 == 1:
                    for k in tmp1:
                        tmp2.append(k + j)
        if len(tmp1) > len(tmp2):
            return tmp1
        else:
            return tmp2

a = Solution()
print a.letterCombinations("23")



