import threading
class Foo(object):
    lock1 = threading.Lock
    lock2 = threading.Lock


    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()
        pass

    def first(self, printFirst):
        """
        :type printFirst: method
        :rtype: void
        """

        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond):
        """
        :type printSecond: method
        :rtype: void
        """
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock2.release()

    def third(self, printThird):
        """
        :type printThird: method
        :rtype: void
        """
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()