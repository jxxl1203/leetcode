# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def rangeSumBST(self, root, L, R):
        def __dfs(node):
            if node:
                if L.val <= node.val <= R.val:
                    self.res += node.val
                if node.val > L.val:
                    __dfs(node.left)
                if node.val < R.val:
                    __dfs(node.right)

        self.res = 0
        __dfs(root)
        return self.res



a = Solution()
nums = [10,5,15,3,7,None,18]
nodes = []
for n in nums:
    if n:
        nodes.append(TreeNode(n))
    else:
        nodes.append(None)
for i in range(len(nodes)/2-2):
    nodes[i].left = nodes[i * 2 + 1]
    nodes[i].right = nodes[i * 2 + 2]
print a.rangeSumBST(nodes[0], nodes[4], nodes[2])