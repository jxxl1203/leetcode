class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)

a = Solution()
print a.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])