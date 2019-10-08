# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        if not root:
            return None
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root

        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val > R:
            return self.trimBST(root.left, L, R)


a = Solution()
nums = [4,3,6,1,2,5,7]

nodes = []
for n in nums:
    nodes.append(TreeNode(n))
for i in range(len(nodes)):
    if i*2+1 < len(nodes):
        nodes[i].left = nodes[i*2+1]
    if i*2+2 < len(nodes):
        nodes[i].right = nodes[i*2+2]

node = a.trimBST(nodes[0],4,5)

def __dfs(node, d):
    print (node.val, d) if node else (None, d)
    if not node:
        return
    __dfs(node.left, d+1)
    __dfs(node.right, d+1)

__dfs(node,1 )