# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def increasingBST(self, root):
        if not root:
            return None
        nodes = []
        def _dfs(root):
            if not root:
                return
            _dfs(root.left)
            nodes.append(root)
            _dfs(root.right)

        _dfs(root)
        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        nodes[-1].left = None
        nodes[-1].right = None
        return nodes[0]
