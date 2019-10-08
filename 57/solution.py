class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        if len(intervals) < 2:
            return intervals
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
print a.insert([],[])
# print a.insert([[1,373],[2,6],[8,10],[15,18],[16,17],[11,22]], [10, 11])
