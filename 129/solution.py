# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):

        self.res = []
        if not root:
            return 0
        def _helper(root, st):
            if not root.left and not root.right:
                self.res.append(st + str(root.val))
                return
            if root.left:
                _helper(root.left, st + str(root.val))
            if root.right:
                _helper(root.right, st + str(root.val))

        _helper(root, "")
        sum = 0
        for s in self.res:
            sum += int(s)
        return sum


a = Solution()
nums = [1,2,3]
nodes = []
for n in nums:
    if n is not None:
        nodes.append(TreeNode(n))
    else:
        nodes.append(None)
for i in range(len(nodes)):
    if nodes[i]:
        if i*2+1 < len(nodes):
            nodes[i].left = nodes[i*2+1]
        if i*2+2 < len(nodes):
            nodes[i].right = nodes[i*2+2]

print a.sumNumbers(nodes[0])