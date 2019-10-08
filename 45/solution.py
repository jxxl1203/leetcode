class Solution(object):
    def jump(self, nums):
        step = 0
        end = 0
        max_jump = 0
        for i in range(len(nums) - 1):
            max_jump = max(max_jump, nums[i] + i)
            if i == end:
                step += 1
                end = max_jump
        return step


a = Solution()
print   a.jump([2,3,1,1,4])