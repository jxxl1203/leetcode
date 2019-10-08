# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        index = nums.index(max(nums))
        root = TreeNode(nums[index])
        if index > 0:
            root.left = self.constructMaximumBinaryTree(nums[:index])
        if index < len(nums)-1:
            root.right = self.constructMaximumBinaryTree(nums[index+1:])
        return root


a = Solution()
root = a.constructMaximumBinaryTree([3,2,1,6,0,5])

def _dfs(root, deep):
    if not root:
        return
    print root.val, deep

    _dfs(root.left, deep+1)
    _dfs(root.right, deep+1)

_dfs(root, 0)