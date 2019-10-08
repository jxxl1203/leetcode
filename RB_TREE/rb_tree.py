class TreeNode(object):

    def __init__(self, val, color):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val
        self.color = color


root = None

def insert(node):
    global root
    if not root:
        root = node
        root.color = 'black'
        return root

    parent = root
    while parent:
        if parent.val < node.val:
            if parent.right:
                parent = parent.right
            else:
                break
        elif parent.val > node.val:
            if parent.left:
                parent = parent.left
            else:
                break
        else:
            pass
    if parent.val == node.val:
        return
    node.color = 'red'
    if parent.val > node.val:
        parent.left = node
    else:
        parent.right = node


def turn_left(node):
    global root
    right_son = node.right
    left_son = right_son.left
    parent = node.parent
    if not parent:
        pass
        # node is root
        root = right_son
    else:

        if parent.left == node:
            parent.left = right_son
        else:
            parent.right = right_son

    right_son.parent = parent
    right_son.left = node
    node.parent = right_son

    node.right = left_son


def turn_right(node):
    global root
    left_son = node.left
    right_son = None

    parent = node.parent
    if not parent:
        root = left_son
    else:
        if parent.left == node:
            parent.left = left_son
        else:
            parent.right = left_son
    if left_son:
        right_son = left_son.right
        left_son.parent = parent
        left_son.right = node
    node.parent = left_son
    node.left = right_son


def fix_up(node):
    global root
    # node is root
    if root == node:
        node.color = 'black'
        return
    parent = node.parent
    cur = node
    #parent is black
    if parent.color == 'black':
        return
    # parent is red and uncle is red
    while cur.color == 'red':
        if not cur.parent:
            cur.color = 'black'
            return

        parent = cur.parent
        if parent.color == 'black':
            return
        grand_parent = parent.parent
        uncle = None
        if grand_parent.left == parent:
            uncle = grand_parent.right
        else:
            uncle = grand_parent.left
        if uncle and uncle.color == 'red':
            parent.color = 'black'
            uncle.color = 'black'
            grand_parent.color = 'red'
            cur = grand_parent
        else:
            if parent.right == cur:
                cur = parent
                turn_left(cur)
            else:
                parent.color = 'black'
                grand_parent.color = 'red'
                turn_right(grand_parent)
                return


def rb_insert(val):
    global root
    if not root:
        root = TreeNode(val, 'black')
    else:
        node = TreeNode(val, 'red')
        tmp = root
        cur = None
        while tmp:
            cur = tmp
            if tmp.val > val:
                tmp = tmp.left
            elif tmp.val < val:
                tmp = tmp.right
            else:
                break
        if cur.val > val:
            cur.left = node
        elif cur.val < val:
            cur.right = node
        node.parent = cur

        fix_up(node)








# nums = [1,2,3,4,5,6,7,8,9,10]
# nodes = []
# for n in nums:
#     if n is not None:
#         nodes.append(TreeNode(n, 'r'))
#     else:
#         nodes.append(None)
# for i in range(len(nodes)):
#     if nodes[i]:
#         if i*2+1 < len(nodes):
#             nodes[i].left = nodes[i*2+1]
#         if i*2+2 < len(nodes):
#             nodes[i].right = nodes[i*2+2]
#         if i > 0:
#             nodes[i].parent = nodes[(i-1)/2]
#
#
def dlr(root, d):
    if not root:
        return
    print root.val, root.color, d
    dlr(root.left, d+1)
    dlr(root.right, d+1)
# root = nodes[0]
# dlr(root, 0)
# print
# # turn_left(nodes[2])
# turn_right(nodes[1])
# dlr(root, 0)

rb_insert(10)
rb_insert(5)
rb_insert(15)
rb_insert(12)
rb_insert(13)
rb_insert(14)
rb_insert(1)
rb_insert(3)

# rb_insert(4)
# rb_insert(5)
dlr(root, 0)