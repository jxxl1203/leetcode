class Solution(object):
    def twoSum(self, nums, target):
        dic = {}
        for i in range(len(nums)):
            if (target - nums[i]) not in dic:
                dic[nums[i]] = i
            else:
                return [dic[target - nums[i]], i]


a = Solution()
print a.twoSum([2, 7, 11, 15], 9)
