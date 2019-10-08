# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 and t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1 or t2




def dfs(node):
    if not node:
        return
    print node.val
    dfs(node.left)
    dfs(node.right)


a = Solution()
nums = [1,3,2,5]
t1 = []
for n in nums:
    if n:
        t1.append(TreeNode(n))
    else:
        t1.append(None)
for i in range(len(t1)):
    if i*2+1 < len(t1):
        t1[i].left = t1[i*2+1]
    if i*2+2 < len(t1):
        t1[i].right = t1[i*2+2]

nums = [2,1,3,None,4,None,7]
# dfs(t1[0])
print
t2 = []
for n in nums:
    if n:
        t2.append(TreeNode(n))
    else:
        t2.append(None)
for i in range(len(t2)):
    if i*2+1 < len(t2):
        t2[i].left = t2[i*2+1]
    if i*2+2 < len(t2):
        t2[i].right = t2[i*2+2]
# dfs(t2[0])

a = Solution()
root = a.mergeTrees(t1[0], t2[0])
#
#
#
dfs(root)
