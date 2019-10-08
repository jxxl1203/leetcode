class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        res = [[0 for i in range(n)] for j in range(m)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        res[0][0] = 1
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1:
                    res[i][j] == 0
                else:
                    if i > 0 and obstacleGrid[i - 1][j] == 0:
                        res[i][j] += res[i - 1][j]
                    if j > 0 and obstacleGrid[i][j - 1] == 0:
                        res[i][j] += res[i][j - 1]
        return res[-1][-1]


a = Solution()
# print a.uniquePathsWithObstacles([[0],[1]])
print a.uniquePathsWithObstacles([
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,1,0]

])
