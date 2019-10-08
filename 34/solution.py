class Solution(object):
    def searchRange(self, nums, target):
        l = 0
        r = len(nums)
        result = []
        while l < r:
            if nums[(l + r) / 2] < target:
                l = (l + r) / 2 + 1
            else:
                r = (l + r) / 2
        if l >= len(nums):
            return [-1, -1]
        elif nums[l] != target:
            return [-1, -1]
        result.append(l)
        r = len(nums)
        while l < r:
            if nums[(l + r) / 2] > target:
                r = (l + r) / 2
            else:
                l = (l + r) / 2 + 1
        result.append(r-1)
        return result


a = Solution()

print a.searchRange([5,7,7,8,8,10], 6)
# print a.searchRange([5,7,7,8,8,8,8,9,9,10,12,12,13,15], 8)