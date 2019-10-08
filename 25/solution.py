class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def reverseKGroup(self, head, k):
        count = 0
        last = head
        while last and count < k:
            last = last.next
            count += 1
        if count == k:
            last = self.reverseKGroup(last, k)
            while count:
                temp = head.next
                head.next = last
                last = head
                head = temp
                count -= 1
            head = last
        return head

    def reverse(self, head):
        if not head or not head.next:
            return head
        new_head = self.reverse(head.next)
        tmp = head.next
        head.next = None
        tmp.next = head
        return new_head

list1 = []
for i in range(1,10):
    list1.append(ListNode(i))

for i in range(len(list1)-1):
    list1[i].next = list1[i+1]


a = Solution()
node_list = a.reverseKGroup(list1[0], 3)
while 1:
    if not node_list:
        break
    print node_list.val
    node_list = node_list.next
