import collections
class Solution(object):
    def topKFrequent(self, words, k):
        dic = collections.defaultdict(int)
        for w in words:
            dic[w] += 1
        que = sorted(dic, key=lambda x: (-dic[x], x))[:k]
        return que


# from heapq import nsmallest
# class Solution:
#     def topKFrequent(self, words, k):
#         counts = {}
#         for i, w in enumerate(words):
#             counts[w] = counts.get(w, 0) + 1
#         print counts
#         return nsmallest(k, counts, lambda i: (-counts[i], i))


a = Solution()
print a.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],4)