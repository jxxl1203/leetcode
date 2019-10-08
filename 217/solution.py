class Solution(object):
    def containsDuplicate(self, nums):
        dic = set()
        for i in nums:
            if i in dic:
                return True
            dic.add(i)
        return False

a = Solution()
print a.containsDuplicate([1,2,3,4,3])