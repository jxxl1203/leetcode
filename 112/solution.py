# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# class Solution(object):
#     def hasPathSum(self, root, sum):
#         if not root:
#             return False
#         self.res = False
#
#         def _helper(root, tmp):
#             tmp += root.val
#             if self.res:
#                 return
#             if not root.left and not root.right and tmp == sum:
#                 self.res = True
#             if root.left:
#                 _helper(root.left, tmp)
#             if root.right:
#                 _helper(root.right, tmp)
#
#         _helper(root, 0)
#         return self.res


class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, sum-root.val)]
        while stack:
            block = stack.pop(0)
            node = block[0]
            if not node.left and not node.right and block[1] == 0:
                return True
            if node.left:
                stack.append((node.left, block[1] - node.left.val))
            if node.right:
                stack.append((node.right, block[1] - node.right.val))
        return False
    
a = Solution()
nums = [5,4,8,11,None,13,4,7,2,None,None,None,1]
# nums = [1,2]
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

print a.hasPathSum(nodes[0], 22)
