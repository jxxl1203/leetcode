
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        front = ListNode(0)
        front.next, fast, last = head, front, front
        while n or fast:
            if n:
                fast = fast.next
                n -= 1
            else:
                fast = fast.next
                last = last.next if fast else last
        last.next = last.next.next
        return front.next


list = []
for i in range(1,6):
    list.append(ListNode(i))
for i in range(0,len(list)-1):
    list[i].next = list[i+1]

a = Solution()
head = a.removeNthFromEnd(ListNode(0), 1)
while head:
    print head.val
    head = head.next
