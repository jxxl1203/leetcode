class Solution(object):
    def topKFrequent(self, nums, k):
        s = set(nums)
        dic = {}
        for i in s:
            dic[i] = 0
        for i in nums:
            dic[i] += 1

        tmp = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        res = []
        for i in range(k):
            res.append(tmp[i][0])
        return res


a = Solution()
print a.topKFrequent([1, 1, 1, 2, 2, 3], 2)
