class Solution(object):
    def minimumTotal(self, triangle):
        for i in range(1, len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j], triangle[i-1][j-1])
        return min(triangle[-1])

a = Solution()
print a.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])