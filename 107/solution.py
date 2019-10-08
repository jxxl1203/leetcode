class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        self.res = []

        def __level(root, deep):
            if not root:
                return
            if len(self.res) < deep:
                self.res.append([])
            self.res[deep-1].append(root.val)
            if root.left:
                __level(root.left, deep+1)
            if root.right:
                __level(root.right, deep+1)
        __level(root, 1)
        self.res.reverse()
        return self.res

a = Solution()
nums = [3,9,20,None,None,15,7]
nodes = []
for n in nums:
    nodes.append(TreeNode(n))
for i in range(len(nodes)):
    if i*2+1 < len(nodes):
        nodes[i].left = nodes[i*2+1]
    if i*2+2 < len(nodes):
        nodes[i].right = nodes[i*2+2]
print a.levelOrderBottom(nodes[0])
