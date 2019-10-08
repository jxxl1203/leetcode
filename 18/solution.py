class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            first = True
            for j in range(i+1, len(nums)):
                if not first and nums[j] == nums[j-1]:
                    continue
                if first:
                    first = False
                tmp = nums[i] + nums[j]
                left = j + 1
                right = len(nums) - 1
                while right > left:
                    if tmp + nums[left] + nums[right] > target:
                        while 1:
                            right -= 1
                            if right <= left or nums[right] != nums[right+1]:
                                break
                    elif tmp + nums[left] + nums[right] < target:
                        while 1:
                            left += 1
                            if left >= right or nums[left] != nums[left-1]:
                                break
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        while 1:
                            right -= 1
                            if right <= left or nums[right] != nums[right+1]:
                                break
                        while 1:
                            left += 1
                            if left >= right or nums[left] != nums[left-1]:
                                break
        return result


a = Solution()
print a.fourSum([0,0,0,0,0,0,0], 0)