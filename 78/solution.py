class Solution(object):
    def subsets(self, nums):
        res = [[]]
        for i in nums:
            res = res + [[i] + num for num in res]
        return res


a = Solution()
print a.subsets([0,1,2])