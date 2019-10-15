# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        node = ListNode(0)
        node.next = head
        pre = node
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = head
            head = head.next
        return node.next
