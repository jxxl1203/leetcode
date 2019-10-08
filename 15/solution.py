class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while r > l:
                if nums[i] + nums[l] + nums[r] > 0:
                    while 1:
                        r -= 1
                        if r <= 0 or nums[r] != nums[r+1]:
                            break
                elif nums[i] + nums[l] + nums[r] < 0:
                    while 1:
                        l += 1
                        if l >= len(nums) or nums[l] != nums[l-1]:
                            break
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while 1:
                        r -= 1
                        if r <= 0 or nums[r] != nums[r+1]:
                            break
                    while 1:
                        l += 1
                        if l >= len(nums) or nums[l] != nums[l-1]:
                            break
        return result



a = Solution()
print a.threeSum([0,0,0,0,0,0,0])
