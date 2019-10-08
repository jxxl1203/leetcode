# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isBalanced(self, root):
        self.res = True

        def _dfs(root):
            if not self.res:
                return
            if not root:
                return 0
            left = _dfs(root.left) + 1
            right = _dfs(root.right) + 1
            if abs(left-right) > 1:
                self.res = False
            return max(left, right)
        _dfs(root)
        return self.res