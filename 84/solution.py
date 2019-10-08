class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []
        stack.append((-1, -1))
        i = 0
        res = 0
        while i < len(heights):
            while stack[-1][1] > heights[i]:
                a = stack.pop()
                area = a[1] * (i - stack[-1][0] - 1)
                if area > res:
                    res = area
            stack.append((i,heights[i]))
            i += 1
        while len(stack) > 1:
            a = stack.pop()
            area = a[1] * (i - stack[-1][0] - 1)
            if area > res:
                res = area
        return res


a = Solution()
print a.largestRectangleArea([6,7,5,2,4,5,9,3])