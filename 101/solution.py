class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        stack = [root,root]
        while stack:
            node1 = stack.pop()
            node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif not node1 or not node2:
                return False
            elif node1.val != node2.val:
                return False
            stack.append(node1.left)
            stack.append(node2.right)
            stack.append(node1.right)
            stack.append(node2.left)
        return True


a = Solution()
nums = [1,2,2,2,None,2]
nodes = []
for n in nums:
    if n is not None:
        nodes.append(TreeNode(n))
    else:
        nodes.append(None)
for i in range(len(nodes)):
    if i*2+1 < len(nodes):
        nodes[i].left = nodes[i*2+1]
    if i*2+2 < len(nodes):
        nodes[i].right = nodes[i*2+2]
print a.isSymmetric(nodes[0])

