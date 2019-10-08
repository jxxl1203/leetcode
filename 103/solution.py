# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        stact  = [root]
        direct = True
        res = []
        while stact:
            vals = []
            tmp = []
            if direct:
                for node in stact:
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                    vals.append(node.val)
                direct = False
            else:
                for i in range(len(stact)-1, -1, -1):
                    node = stact[i]
                    if node.left:
                        tmp.append(node.left)
                    if node.right:
                        tmp.append(node.right)
                    vals.append(node.val)
                direct = True
            stact = tmp
            res.append(vals)
        return res

a = Solution()
nums = [1,2,3,4,None,None,5]
nodes = []
