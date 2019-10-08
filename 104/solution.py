# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    max_deep = 0

    def maxDepth(self, root):
        if root == None:
            return 0

        self.max_deep == 0

        def __dfs(node, deep):
            print node.val
            if deep > self.max_deep:
                self.max_deep = deep
            if node.left != None:
                __dfs(node.left, deep + 1)
            if node.right != None:
                __dfs(node.right, deep + 1)

        __dfs(root, 1)
        return self.max_deep



a = Solution()
nums = [3,9,20,None ,None,15,7]
nodes = []
for i in len(nums):
    if not nums[i]:
        node = TreeNode(nums[i])
        if i > 0:
            if i % 2 == 0:
                nodes[i - 1]