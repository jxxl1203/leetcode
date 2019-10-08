class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):
    def preorder(self, root):
        self.res = []
        self.search(root)
        return self.res

    def search(self, root):
        if root is None:
            return
        self.res.append(root.val)
        for i in root.children:
            self.search(i)