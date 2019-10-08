class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        if not head:
            return head
        while head and head.val is not None:
            head.val = None
            head = head.next
        return head.next