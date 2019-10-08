# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         node_set = set()
#         while headA:
#             node_set.add(headA)
#             headA = headA.next
#         while headB:
#             if headB in node_set:
#                 return headB
#             headB = headB.next
#         return None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        node1 = headA
        node2 = headB
        end1 = 0
        while node1 != node2:
            if end1 > 1:
                return None
            node1 = node1.next
            node2 = node2.next
            if not node1:
                node1 = headB
                end1 += 1
            if not node2:
                node2 = headA
        return node1