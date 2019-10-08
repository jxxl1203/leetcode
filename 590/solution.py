class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Solution(object):

    def postorder(self, root):
        self.res = []
        def __lrd(root):
            if not root:
                return
            for node in root.children:
                __lrd(node)
            self.res.append(root.val)

        __lrd(root)
        return self.res

