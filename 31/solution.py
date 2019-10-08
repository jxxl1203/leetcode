class Solution(object):
    def nextPermutation(self, nums):
        index = 0
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                index = i
                break
        for i in range(index, len(nums) - (len(nums) - index) / 2):
            nums[i], nums[len(nums) - (i - index + 1)] = nums[len(nums) - (i - index + 1)],  nums[i]
        if index > 0:
            for i in range(index, len(nums)):
                if nums[i] > nums[index-1]:
                    nums[i], nums[index-1] = nums[index-1], nums[i]
                    break
        return nums




a = Solution()
print a.nextPermutation([1,2,3,2,1])