import copy
class Solution(object):
    res = []

    def combine(self, n, k):
        self.res = []

        def __dfs(st, n, k, arr):
            if len(arr) == k:

                self.res.append(copy.deepcopy(arr))
                return
            if st > n:
                return
            __dfs(st + 1, n, k, arr)
            arr.append(st)
            __dfs(st + 1, n, k, arr)
            arr.pop()
        __dfs(1, n, k, [])
        return self.res

a = Solution()
print a.combine(0, 0)