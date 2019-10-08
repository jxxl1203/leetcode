class Solution(object):
    def canJump(self, nums):
        # if len(nums) < 2:
        #     return True
        i = len(nums) - 2
        while i > -1:
            if nums[i] == 0:
                j = i-1
                while j > -1:
                    if nums[j] + j > i:
                        break
                    j -= 1
                if j == -1:
                    return False
            i -= 1
        return True

a = Solution()
print a.canJump([])