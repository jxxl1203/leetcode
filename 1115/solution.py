import threading


class FooBar(object):

    lock_foo = threading.Lock
    lock_bar = threading.Lock

    def __init__(self, n):
        self.n = n
        self.lock_foo = threading.Lock()
        self.lock_bar = threading.Lock()

        self.lock_bar.acquire()

    def foo(self, printFoo):
        """
        :type printFoo: method
        :rtype: void
        """
        for i in xrange(self.n):
            # printFoo() outputs "foo". Do not change or remove this line.
            self.lock_foo.acquire()
            printFoo()
            self.lock_bar.release()

    def bar(self, printBar):
        """
        :type printBar: method
        :rtype: void
        """
        for i in xrange(self.n):
            self.lock_bar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.lock_foo.release()

def printBar():
    print "bar"
def printFoo():
    print "foo"
a = FooBar(1)

ta = threading.Thread(target=a.foo, args=[printFoo])
tb = threading.Thread(target=a.bar, args=[printBar])
ta.start()
tb.start()