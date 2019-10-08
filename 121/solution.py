class Solution(object):
    def maxProfit(self, prices):
        res = 0
        max_num = 0
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_num:
                max_num = prices[i]
            if max_num - prices[i] > res:
                res = max_num - prices[i]
        return res


a = Solution()
print a.maxProfit([7,6,4,3,1])
