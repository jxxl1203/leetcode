class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        while head.next and head.val is not None:
            head.val = None
            head = head.next
        if not head.next:
            return False
        return True


a = Solution()
s = [1,2,3,0,5]
nodes = []
for i in range(len(s)):
    nodes.append(ListNode(s[i]))
    if i > 0:
        nodes[i-1].next = nodes[i]

print a.hasCycle(nodes[0])
