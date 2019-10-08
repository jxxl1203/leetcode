class Solution(object):
    def firstMissingPositive(self, nums):
        has_one = 0
        for a in nums:
            if a == 1:
                has_one += 1
        if has_one == 0:
            return 1

        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = 1
        for i in range(n):
            val = abs(nums[i])
            if val == n:
                nums[0] = -abs(nums[0])
            else:
                nums[val] = -abs(nums[val])

        for i in range(1, n):
            if nums[i] > 0:
                return i
        if nums[0] > 0:
            return n
        return n + 1


a = Solution()
print a.firstMissingPositive([1,7,8,9,11,12])