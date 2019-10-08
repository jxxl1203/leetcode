# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        if k == 0:
            return head
        if not head:
            return head

        i = 1
        end = head
        while end.next:
            i += 1
            end = end.next
        tmp = head
        j = 1
        k = k % i
        while i > k + j:
            tmp = tmp.next
            j += 1
        end.next = head
        res = tmp.next
        tmp.next = None
        return res

a = Solution()
nodes = []
for i in range(1,6):
    nodes.append(ListNode(i))
for i in range(4):
    nodes[i].next = nodes[i+1]
head = a.rotateRight(nodes[0],0)

while head:
    print head.val
    head = head.next
