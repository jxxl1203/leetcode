class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteNode(self, node):
        while 1:
            node.val = node.next.val
            if not node.next.next:
                node.next = None
                return
            node = node.next

