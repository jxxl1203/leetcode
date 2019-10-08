# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):

    def levelOrder(self, root):
        self.res = []
        def __level(root, deep):
            if not root:
                return
            if len(self.res) < deep:
                self.res.append([])
            self.res[deep-1].append(root.val)
            for i in root.children:
                __level(i, deep+1)
        __level(root, 1)
        return self.res