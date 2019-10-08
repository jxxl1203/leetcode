class Solution(object):
    def removeElement(self, nums, val):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


a = Solution()
nums = [1,2,2,3,4,2,3,2,2,2,1]
l = a.removeElement(nums, 2)
print l
for i in range(l):
    print nums[i],