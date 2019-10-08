class Solution(object):
    def sortColors(self, nums):
        zero, one, two = 0, 0, len(nums) - 1
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else:
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1
        return nums

a = Solution()
print a.sortColors([1,2,1,2,1,2,0,0,0])