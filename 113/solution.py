# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        res = []
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            block = stack.pop(0)
            node = block[0]
            s_tmp = block[1]
            if not node.left and not node.right and s_tmp == 0:
                res.append(block[2])
            if node.left:
                list = block[2] + [node.left.val]

                stack.append((node.left, s_tmp - node.left.val, list))
            if node.right:
                list = block[2] + [node.right.val]
                stack.append((node.right, s_tmp - node.right.val, list))
        return res