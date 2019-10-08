# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next



class Solution(object):
    def connect(self, root):
        cur = root
        while cur:
            head = Node(0,None,None,None)
            tail = head
            while cur:
                if cur.left:
                    tail.next = cur.left
                    tail = tail.next
                if cur.right:
                    tail.next = cur.right
                    tail = tail.next
                cur = cur.next
            cur = head.next
        return root




        return root


a = Solution()
nums = [1,2,3,4,5]
nodes = []
for n in nums:
    if n:
        nodes.append(Node(n,None, None, None))
    else:
        nodes.append(None)

for i in range(len(nodes)):
    if nodes[i]:
        if i * 2 + 1 < len(nodes):
            nodes[i].left = nodes[i*2+1]
        if i * 2 + 2 < len(nodes):
            nodes[i].right = nodes[i*2+2]

a.connect(nodes[0])