# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):

        def _change(left, right):

            if left > right:
                return None
            mid = left + (right - left) / 2
            root = TreeNode(nums[mid])
            root.left = _change(left, mid - 1)
            root.right = _change(mid + 1, right)
            return root
        return _change(0, len(nums)-1)


a = Solution()
print a.sortedArrayToBST([-10,-3,0,5,9])