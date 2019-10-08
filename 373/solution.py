
# import heapq
# class Solution(object):
#     def kSmallestPairs(self, nums1, nums2, k):
#         heap = []
#         for i in range(min(k, len(nums1))):
#             for j in range(min(k, len(nums2))):
#                 heap.append([nums1[i], nums2[j]])
#         return heapq.nsmallest(k, heap, key= lambda x: x[0]*x[1])



class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        import heapq
        res = []
        visited = set()
        n, m = len(nums1), len(nums2)
        if n*m*k == 0:
            return res
        s = 1
        k = min(k, m*n)
        h = [(nums1[0] + nums2[0], 0, 0)]
        visited.add(( 0, 0))
        while s <= k:
            item = heapq.heappop(h)
            i, j = item[1], item[2]
            res.append([nums1[i], nums2[j]])
            if i < n-1 and (i+1, j) not in visited:
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1, j))
            if j < m-1 and (i, j+1) not in visited:
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))
                visited.add((i, j+1))
            s += 1
        return res





a = Solution()
print a.kSmallestPairs([], [2,4,6], 3)