# class Solution(object):
#     def canCompleteCircuit(self, gas, cost):
#         l = len(gas)
#         last = [0] * l
#         sum = 0
#         for i in range(l):
#             last[i] = gas[i] - cost[i]
#             sum += last[i]
#         if sum < 0:
#             return -1
#         for i in range(l):
#             if last[i] >= 0:
#                 p = i
#                 last_gas = 0
#                 while last_gas >= 0:
#                     last_gas += last[p]
#                     p = (p + 1) % l
#                     if p == i:
#                         return i
#         return -1

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        sum, result, has_result = 0, 0, 0
        for i in range(len(gas)):
            has_result += gas[i] - cost[i]
            sum += gas[i] - cost[i]
            if sum < 0:
                result = i+1
                sum = 0
        return result if has_result >= 0 else -1

a = Solution()
print a.canCompleteCircuit([5,8,2,8], [6,5,6,6])
