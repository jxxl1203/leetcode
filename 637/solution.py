# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        self.res = []
        def _dfs(root, deep):
            if not root:
                return
            if len(self.res) <= deep:
                self.res.append([0,0])
            self.res[deep][0] += 1
            self.res[deep][1] += root.val
            _dfs(root.left, deep+1)
            _dfs(root.right, deep+1)

        _dfs(root, 0)
        res = []
        for i, num in self.res:
            res.append(float(num)/float(i))
        return res