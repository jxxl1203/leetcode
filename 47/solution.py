class Solution(object):
    def permuteUnique(self, nums):
        res_set = set()
        result = []
        def recall(arrs, tmp):
            if not arrs:
                res_set.add(tmp)
                return
            for i in range(len(arrs)):
                recall(arrs[:i] + arrs[i+1:], tmp + "," + str(arrs[i]))
        recall(nums, "")
        for s in res_set:
            a = []
            for ss in s[1:].split(","):
                a.append(int(ss))
            result.append(a)
        return result


a = Solution()
print a.permuteUnique([1,1,3])