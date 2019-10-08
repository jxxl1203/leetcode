class Solution(object):
    def multiply(self, num1, num2):
        res = [0] * (len(num1) * len(num2) + 1)
        n1 = [0] * len(num1)
        n2 = [0] * len(num2)
        index = 0
        result = ""
        if num1 == "0" or num2 == "0":
            return "0"
        elif num1 == "1":
            return num2
        elif num2 == "1":
            return num1
        for i in range(len(num1) - 1, -1, -1):
            n1[len(num1) - i - 1] = int(num1[i])
        for i in range(len(num2) - 1, -1, -1):
            n2[len(num2) - i - 1] = int(num2[i])
        for i in range(len(n1)):
            for j in range(len(n2)):
                res[i+j] += n1[i] * n2[j]
                res[i+j+1] += res[i+j] / 10
                res[i+j] = res[i+j] % 10
                index = max(index, i+j+1)
        if res[index] == 0:
            index -= 1
        for i in range(index, -1, -1):
            result += str(res[i])
        return result

a = Solution()
print a.multiply("123", "456")