# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        fast = head
        slow = head
        pre = None
        while fast and fast.next:
            fast = fast.next.next
            pre = slow
            slow = slow.next
        if pre:
            pre.next = None
        node = TreeNode(slow.val)
        if head == slow:
            return node
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node


a = Solution()
nums = [-10, -3, 0, 5, 9]
nodes = []
for n in nums:
    nodes.append(ListNode(n))
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i+1]

root = a.sortedListToBST(nodes[0])
print root
def _dlr(root):
    if not root:
        return
    print root.val
    _dlr(root.left)
    _dlr(root.right)

_dlr(root)