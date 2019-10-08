# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal1(self, root):
        if not root:
            return []
        res = []
        def _lbr(node):
            if not node:
                return
            _lbr(node.left)
            res.append(node.val)
            _lbr(node.right)
        _lbr(root)
        return res

    def inorderTraversal(self, root):
        list = []
        stack = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            list.append(root.val)
            root = root.right
        return list

a = Solution()
nums = [1,2,3,4,5,6,7]
nodes = []
for n in nums:
    if n is not None:
        nodes.append(TreeNode(n))
for i in range((len(nums)-2)/2+1):
    if nodes[i]:
        nodes[i].left = nodes[i*2+1]
        nodes[i].right = nodes[i*2+2]
print a.inorderTraversal(nodes[0])