class Solution(object):
    def trap(self, height):
        max_left = [0] * len(height)
        max_right = [0] * len(height)
        for i in range(1, len(height)):
            max_left[i] = max(max_left[i-1], height[i-1])
        for i in range(len(height)-2, 0, -1):
            max_right[i] = max(max_right[i+1], height[i+1])
        result = 0
        for i in range(1, len(height) - 1):
            water = min(max_left[i], max_right[i])
            if water > height[i]:
                result += water - height[i]
        return result


a = Solution()
print a.trap([0,1,0,2,1,0,1,3,2,1,2,1])