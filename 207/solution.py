from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        sides = defaultdict(set)
        in_sides = [0] * numCourses
        for i, j in prerequisites:
            sides[i].add(j)
            in_sides[j] += 1
        queue = []
        for i in range(numCourses):
            if in_sides[i] == 0:
                queue.append(i)
        count = 0
        while queue:
            d = queue.pop(0)
            count += 1
            for s in sides[d]:
                in_sides[s] -= 1
                if in_sides[s] == 0:
                    queue.append(s)
        return count == numCourses


a = Solution()
print a.canFinish(2, [[1, 0], [0, 1]])