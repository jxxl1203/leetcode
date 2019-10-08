class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def maxDepth(self, root):
        self.deep = 0
        def _search(root, d):
            if not root:
                return
            if d > self.deep:
                self.deep = d
            for i in root.children:
                _search(i, d+1)
        _search(root, 1)
        return self.deep


