class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def __merge(head1):
            if not head1:
                return
            slow = head1
            fast = head1
            while fast:
                if fast.next and fast.next.next:
                    fast = fast.next.next
                else:
                    break
                slow = slow.next
            tmp = slow.next
            slow.next = None

            __merge(head1)
            __merge(tmp)
            new_head = ListNode(0)
            while head1 and tmp:
                if head1.val > tmp.val:
                    new_head.next = tmp
                else:
                    new_head.next = head1
                new_head = new_head.next
            if head1:
                new_head.next = head1
            if tmp:
                new_head.next = tmp
            
