class Solution(object):
    def findKthLargest(self, nums, k):
        # def partition(start, end):
        #     left = start
        #     right = end
        #     mid = nums[left]
        #     while left < right:
        #         while left < right and nums[right] <= mid:
        #             right -= 1
        #         nums[left] = nums[right]
        #         while left < right and nums[left] >= mid:
        #             left += 1
        #         nums[right] = nums[left]
        #     nums[left] = mid
        #     return right
        #
        # l = len(nums) - 1
        # idx = partition(0, l)
        # while 1:
        #     if idx == k - 1:
        #         return nums[idx]
        #     elif idx < k:
        #         idx = partition(idx + 1, l)
        #     else:
        #         idx = partition(0, idx - 1)
        nums.sort(reverse=True)
        return nums[k-1]



a = Solution()
nums = [6,4,2,8,0,5,2,8,2]
print a.findKthLargest(nums, 1)
