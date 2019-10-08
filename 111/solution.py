# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        stack = [root]
        min_deep = 0
        while stack:
            tmp = []
            min_deep += 1
            for node in stack:
                if not node.left and not node.right:
                    return min_deep
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            stack = tmp
        return min_deep
