class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []
        start = []
        end = []
        res = []
        for dist in intervals:
            start.append(dist[0])
            end.append(dist[1])
        start.sort()
        end.sort()
        i = 1
        h, e = start[0], end[0]
        while i < len(intervals):
            if start[i] > e:
                res.append([h, e])
                h = start[i]
                e = end[i]
            else:
                e = end[i]
            i += 1
        res. append([h, e])
        return res


a = Solution()
print a.merge([[1,3],[2,6],[8,10],[15,18],[16,17],[11,22]])
