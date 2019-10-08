class Solution(object):
    def lastStoneWeight(self, stones):
        while len(stones) > 1:
            stones.sort()
            a = stones.pop()
            b = stones.pop()
            if a > b:
                stones.append(a-b)
        return stones[0] if len(stones) == 1 else 0


a = Solution()
print a.lastStoneWeight([2,7,4,1,8,1])