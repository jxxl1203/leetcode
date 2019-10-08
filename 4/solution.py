class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)
        left = 0
        right = n1
        while left < right:
            i = left + (right - left) // 2
            j = (n1 + n2 + 1) // 2 - i

            if nums1[i] < nums2[j - 1]:
                left = i + 1
            else:
                right = i

        m1 = left
        m2 = (n1+n2+1)//2-m1
        r1 = max(nums1[m1-1] if m1 > 0 else float("-inf"), nums2[m2-1] if m2 > 0 else float("-inf"))
        if (n1+n2) % 2 == 1:
            return r1
        r2 = min(nums1[m1] if m1 < n1 else float("inf"), nums2[m2] if m2 <n2 else float("inf"))
        return (r1+r2) / 2.0


# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         num = nums1 + nums2
#         num.sort()
#         l = len(num)
#         if l % 2 == 0:
#             return float((num[l/2] + num[l/2-1]) / 2.0)
#         else:
#             return float(num[l/2])

s = Solution()
nums1 = [1, 2]
nums2 = [3, 4]

a = s.findMedianSortedArrays(nums1, nums2)
print a

