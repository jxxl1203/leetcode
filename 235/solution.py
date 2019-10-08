class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val > q.val:
            p, q = q, p
        while 1:
            if p.val <= root.val <= q.val:
                return root
            if p.val <= q.val < root.val:
                root = root.left
            else:
                root = root.right


a = Solution()
nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
nodes = []
for i in range(len(nums)):
    nodes.append(TreeNode(nums[i]))
for i in range(len(nums), -1, -1):
    if 2 * i + 2 < len(nums):
        nodes[i].right = nodes[2 * i + 2]
    if 2 * i + 1 < len(nums):
        nodes[i].left = nodes[2 * i + 1]
# def _dlr(root):
#     if not root:
#         return
#     print root.val
#     _dlr(root.left)
#     _dlr(root.right)
# _dlr(nodes[0])

node = a.lowestCommonAncestor(nodes[0], nodes[5], nodes[6])
print node.val