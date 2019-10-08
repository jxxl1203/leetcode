import copy
class Solution(object):
    target = 0
    candidates = []
    result = []
    tmp = []

    def combinationSum(self, candidates, target):
        self.target = target
        candidates.sort()
        self.candidates = candidates
        self.result = []
        self.tmp = []
        self.dp(0, 0)
        return self.result

    def dp(self, start, sum):
        if sum > self.target:
            return
        for i in range(start, len(self.candidates)):
            a = self.candidates[i]
            if sum + a < self.target:
                self.tmp.append(a)
                self.dp(i, sum + a)
                self.tmp.pop()
            elif sum + a == self.target:
                temp = copy.deepcopy(self.tmp)
                temp.append(a)
                self.result.append(temp)
            else:
                return
a = Solution()
print a.combinationSum([5, 3, 2], 8)