class Solution(object):
    def isValid(self, s):
        left = {"(": 1, "[": 2, "{": 3}
        right = {")": 1, "]": 2, "}": 3}
        stack = Stack()
        for c in s:
            if c == " ":
                continue
            elif c in left:
                stack.push(c)
            elif c in right:
                if stack.size() == 0 or left[stack.pop()] != right[c]:
                    return False
        if stack.size() == 0:
            return True
        else:
            return False


class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

a =Solution()
print a.isValid("}")