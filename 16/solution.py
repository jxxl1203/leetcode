class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_dist = 9223372036854775807
        result = 0
        flag = False
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                sum = nums[i] + nums[l] + nums[r]
                if sum > target:
                    r -= 1
                    if sum - target < min_dist:
                        min_dist = sum - target
                        result = sum
                elif sum < target:
                    l += 1
                    if target - sum < min_dist:
                        min_dist = target - sum
                        result = sum
                else:
                    return sum
        return result


a = Solution()
print a.threeSumClosest([0,2,1,-3], 1)


