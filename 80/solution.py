class Solution(object):
    def removeDuplicates(self, nums):
        current = 1
        for i in range(2, len(nums)):
            if nums[i] != nums[current - 1]:
                nums[current + 1] = nums[i]
                current += 1
        return current + 1

a = Solution()
nums = [1,1,1,1,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,5,5]
print a.removeDuplicates(nums)
print nums