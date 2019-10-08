class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums)
        while l < r:
            mid = (l + r) / 2
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

a = Solution()
print a.searchInsert([1,3,5,6], 2)
