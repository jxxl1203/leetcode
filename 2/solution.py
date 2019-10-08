# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        node = ListNode(0)
        res = node
        carry = False
        while True:
            if not carry and not l1 and not l2:
                return res.next
            val = 0
            if carry:
                val = 1
            if l1:
                val += l1.val
            if l2:
                val += l2.val

            if val >= 10:
                carry = True
                val -= 10
            else:
                carry = False

            nex = ListNode(val)
            node.next = nex
            node = node.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next


a = Solution()
nums1 = [2, 4, 3]
nums2 = [5, 6, 4]
nodes1 = []
nodes2 = []
for n in nums1:
    nodes1.append(ListNode(n))
for n in nums2:
    nodes2.append(ListNode(n))
for i in range(len(nodes1)-1):
    nodes1[i].next = nodes1[i+1]
for i in range(len(nodes2)-1):
    nodes2[i].next = nodes2[i+1]

head = a.addTwoNumbers(nodes1[0], nodes2[0])
while head:
    print head.val,
    head = head.next