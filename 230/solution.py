class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution(object):

    def __init__(self):
        self.count = 0
        self.res = 0

    def kthSmallest(self, root, k):

        def __ldr(root):
            if self.count == k:
                return
            if root.left:
                self.kthSmallest(root.left, k)

            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            if root.right:
                self.kthSmallest(root.right, k)
        __ldr(root)
        return self.res


