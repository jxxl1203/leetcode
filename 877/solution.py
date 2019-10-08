# class Solution(object):
#     def stoneGame(self, piles):
#         return True

class Solution(object):
    def stoneGame(self, piles):
        l = len(piles)
        res = [[0 for i in range(l)] for j in range(l)]
        for i in range(l):
            res[i][i] = piles[i]
        for i in range(0, l-1):
            res[i][i+1] = abs(piles[i] - piles[i+1])
        for i in range(l-2):
            for j in range(i, l):
                res[i][j] = max(res[i+1][j] + piles[i], res[i][j-1] + piles[j])
        return res[0][l-1]