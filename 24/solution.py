class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        node = head
        list = []

        while node:
            list.append(node)
            node = node.next
        l = len(list)
        for i in range(l):
            if i % 2 == 0 and i + 3 < l:
                list[i].next = list[i+3]
            elif i % 2 == 1:
                list[i].next = list[i-1]
            elif i+2 < l:
                list[i].next = list[i+2]
            else:
                list[i].next = None
        return list[1] if l > 1 else head


list1 = []
for i in range(1,6):
    list1.append(ListNode(i))

for i in range(len(list1)-1):
    list1[i].next = list1[i+1]


a = Solution()
node_list = a.swapPairs(list1[0])
while 1:
    if not node_list:
        break
    print node_list.val
    node_list = node_list.next