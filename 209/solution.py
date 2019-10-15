class Solution(object):
    def minSubArrayLen(self, s, nums):
        left, right, sum, l = 0, 0, 0, len(nums)
        while sum < s and right < l:
            sum += nums[right]
            right += 1
        if sum < s:
            return 0
        res = right - left + 1
        while right < l:
            sum += nums[right]
            while 1:
                if sum - nums[left] >= s:
                    sum -= nums[left]
                    left += 1
                else:
                    break
            res = min(res, right - left + 1)
            right += 1
        return res


a = Solution()
print a.minSubArrayLen(9, [1,1,9,2,7,1])