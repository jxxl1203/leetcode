class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                i += 1
                nums[i] = nums[j]
        return i + 1


a = Solution()
nums = [1,2,2,3,4]
l = a.removeDuplicates(nums)
print l
for i in range(l):
    print nums[i],