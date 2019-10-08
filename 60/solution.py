class Solution(object):
    factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    res = []

    def getPermutation(self, n, k):
        nums = [i + 1 for i in range(n)]
        self.__dfs(nums, [], k, 0)
        return "".join([str(i) for i in self.res])

    def __dfs(self, nums, tmp, k, index):
        if index == k or len(nums) == 0:
            self.res = tmp + nums
            return
        n = len(nums)
        i = 0
        while index + self.factorial[n-1] < k:
            index += self.factorial[n - 1]
            i += 1
        # if index == k:
        #     i -= 1
        tmp.append(nums[i])
        nums = nums[:i] + nums[i+1:]
        self.__dfs(nums, tmp, k, index)


a = Solution()
print a.getPermutation(4,10)