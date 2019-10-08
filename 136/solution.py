class Solution(object):
    def singleNumber(self, nums):
        res = 0
        for a in nums:
            res = res ^ a
        return res


a = Solution()
print a.singleNumber([4,1,2,1,2,4,5])