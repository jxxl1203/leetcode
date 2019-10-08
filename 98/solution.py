# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        last = float('-inf')
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= last:
                return False
            last = root.val
            root = root.right
        return True


a = Solution()
nums = [10, 5, 15, None, None, 6, 20]
nodes = []
for n in nums:
    if n is not None:
        nodes.append(TreeNode(n))
    else:
        nodes.append(None)
for i in range(len(nodes)):
    if i * 2 + 1 < len(nodes):
        nodes[i].left = nodes[i * 2 + 1]
    if i * 2 + 2 < len(nodes):
        nodes[i].right = nodes[i * 2 + 2]
print a.isValidBST(nodes[0])
