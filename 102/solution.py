# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def levelOrder(self, root):
#         res = []
#         def _dfs(root, d):
#             if not root:
#                 return
#             if len(res) <= d:
#                 res.append([root.val])
#             else:
#                 res[d].append(root.val)
#             _dfs(root.left, d+1)
#             _dfs(root.right, d+1)
#         _dfs(root, 0)
#         return res


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        stack = [root]
        res = []
        while stack:
            vals = []
            tmp = []
            for node in stack:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
                vals.append(node.val)
            stack = tmp
            res.append(vals)
        return res
