# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        def _max_dist(root):
            global res
            if not root:
                return 0
            max_left = max(_max_dist(root.left), 0)
            max_right = max(_max_dist(root.right), 0)
            res = max(res, root.val+max_left+max_right)
            return root.val + max(max_left, max_right)
        global res
        res = float('-inf')
        _max_dist(root)
        return res





a = Solution()
a.maxPathSum(TreeNode(0))