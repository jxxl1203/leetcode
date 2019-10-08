import sys
class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_num = sys.maxint

    def push(self, x):
        self.stack.append(x)
        if x < self.min_num:
            self.min_num = x

    def pop(self):
        """
        :rtype: None
        """
        a = self.stack[-1]
        self.stack = self.stack[:-1]
        if a == self.min_num:
            self.min_num = sys.maxint
            for i in self.stack:
                if i < self.min_num:
                    self.min_num = i

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_num


obj = MinStack()
obj.push(1)
obj.push(2)
obj.push(3)
obj.pop()
print obj.top()
