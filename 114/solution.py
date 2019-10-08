# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        res = root
        while root:
            if root.left:
                son_right = root.left
                while son_right.right:
                    son_right = son_right.right
                son_right.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        return res