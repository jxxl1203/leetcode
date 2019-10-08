

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        dist = 1
        l = len(lists)
        while dist < l:
            for i in range(0, l-dist, dist * 2):
                lists[i] = self.mergeTwoLists(lists[i], lists[i+dist])
            dist *= 2
        return lists[0] if l > 0 else lists

    def mergeTwoLists(self, l1, l2):
        print l1
        print l2
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1 or l2


list1 = []
list2 = []
list3 = []
for i in range(1,5):
    list1.append(ListNode(i))
    list2.append(ListNode(i+1))
    list3.append(ListNode(i+3))
for i in range(len(list1)-1):
    list1[i].next = list1[i+1]
    list2[i].next = list2[i+1]
    list3[i].next = list3[i+1]

a = Solution()
# node_list = a.mergeKLists([list1[0], list2[0], list3[0]])
node_list = a.mergeKLists([])

while 1:
    if not node_list:
        break
    print node_list.val
    node_list = node_list.next