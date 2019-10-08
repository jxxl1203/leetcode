# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        l = []
        r = []
        for i in range(1, len(preorder)):
            if preorder[i] < root.val:
                l += [preorder[i]]
            else:
                r += [preorder[i]]
        root.left = self.bstFromPreorder(l)
        root.right = self.bstFromPreorder(r)
        return root


a = Solution()
root = a.bstFromPreorder([8,5,1,7,10,12])
def _dfs(root, d):
    if not root:
        return
    print (root.val, d)
    _dfs(root.left, d+1)
    _dfs(root.right, d+1)

_dfs(root, 0)