class Solution(object):
    def productExceptSelf(self, nums):
        l = len(nums)
        res = [1] * l
        left = 1
        right = 1
        for i in range(l):
            res[i] *= left
            left *= nums[i]
            res[l - 1 - i] *= right
            right *= nums[l - 1 - i]
        return res

a = Solution()
print a.productExceptSelf([2,4,56,7,8,9,8,5,43,45])