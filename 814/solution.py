class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pruneTree(self, root):
        if not root:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if not root.left and not root.right and root.val == 0:
            return None
        return root


a = Solution()
nums = [1,1,0,1,1,0,1,0]
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
root = a.pruneTree(nodes[0])

def dfs(root):
    if not root:
        return
    print root.val
    dfs(root.left)
    dfs(root.right)

dfs(root)