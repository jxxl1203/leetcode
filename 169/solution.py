# class Solution(object):
#     def majorityElement(self, nums):
#         nums.sort()
#         return nums[len(nums)/2]
class Solution(object):
    def majorityElement(self, nums):
        num = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == num:
                count += 1
            else:
                count -= 1
                if count == 0:
                    num = nums[i]
                    count = 1
        return num