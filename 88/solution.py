class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i = len(nums1) - 1
        m = m - 1
        n = n - 1
        while m >= 0 and n >= 0:
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m -= 1
            else:
                nums1[i] = nums2[n]
                n -= 1
            i -= 1
        if n >= 0:
            for i in range(n, -1, -1):
                nums1[i] = nums2[i]
        return nums1


a = Solution()
print a.merge([0], 0, [3],1)
