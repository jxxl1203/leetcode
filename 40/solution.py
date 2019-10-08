import copy
class Solution(object):
    target = 0
    candidates = []
    result = []
    tmp = ""

    def combinationSum2(self, candidates, target):
        self.target = target
        candidates.sort()
        self.candidates = candidates
        self.result = []
        self.tmp = ""
        self.dp(0, 0)
        self.result = list(set(self.result))
        ans = []
        for str in self.result:
            str = str[1:]
            split = str.split(",")
            tmp = []
            for s in split:
                tmp.append(int(s))
            ans.append(tmp)
        return ans

    def dp(self, start, sum):
        if sum > self.target:
            return
        for i in range(start, len(self.candidates)):
            a = self.candidates[i]
            if sum + a < self.target:
                self.tmp += "," + str(a)
                self.dp(i + 1, sum + a)
                end = self.tmp.rfind(",")
                self.tmp = self.tmp[:end]
            elif sum + a == self.target:
                var = self.tmp + "," + str(a)
                self.result.append(var)
            else:
                return


a = Solution()
print a.combinationSum2([2,5,2,1,2], 5)
