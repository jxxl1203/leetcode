class Solution(object):
    def permute(self, nums):
        result = []

        def recall(arrs, tmp):
            if not arrs:
                result.append(tmp)
                return
            for i in range(len(arrs)):
                recall(arrs[:i] + arrs[i+1:], tmp + [arrs[i]])
        recall(nums, [])
        return result


a = Solution()
print a.permute([1,2,3])