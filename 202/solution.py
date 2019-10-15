# class Solution(object):
#     def isHappy(self, n):
#         s = str(n)
#         history = set()
#         while s != "1":
#             if s in history:
#                 return False
#             history.add(s)
#             sum = 0
#             for c in s:
#                 sum += int(c)**2
#             s = str(sum)
#         return True


class Solution(object):
    def isHappy(self, n):
        history = set()
        while n != 1:
            sum = 0
            while n:
                sum += (n % 10) ** 2
                n //= 10
            if sum in history:
                return False
            else:
                history.add(sum)
            n = sum
        return True

a = Solution()
print a.isHappy(19)
