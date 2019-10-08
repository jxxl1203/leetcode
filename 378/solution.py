class Solution(object):
    def kthSmallest(self, matrix, k):
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left != right:
            mid = (left + right) / 2
            i = len(matrix) - 1
            j = 0
            count = 0
            while i >= 0 and j < len(matrix):
                if matrix[i][j] <= mid:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
            if count >= k:
                right = mid
            else:
                left = mid + 1
        return right


a = Solution()
print a.kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
], 8)