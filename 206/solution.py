class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        curr = head
        last = None
        while curr:
            tmp = curr.next
            curr.next = last
            last = curr
            curr = tmp
        return last


a = Solution()
s = [1,2,3,4,5]
nodes = []
for i in s:
    nodes.append(ListNode(i))
for i in range(4):
    nodes[i].next = nodes[i + 1]

head = a.reverseList(nodes[0])
while head:
    print head.val
    head = head.next