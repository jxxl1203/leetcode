# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0:
            return None

        root = TreeNode(preorder[0])
        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                root.left = self.buildTree(preorder[1:i+1], inorder[:i])
                root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root


