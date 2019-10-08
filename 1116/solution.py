import threading
class ZeroEvenOdd(object):
    odd_lock , even_lock, zero_lock = threading.Lock, threading.Lock, threading.Lock
    def __init__(self, n):
        self.odd_lock = threading.Lock()
        self.even_lock = threading.Lock()
        self.zero_lock = threading.Lock()
        self.odd_lock.acquire()
        self.even_lock.acquire()
        self.n = n

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):

            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.even_lock.release()
            else:
                self.odd_lock.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n + 1, 2):
            self.even_lock.acquire()
            printNumber(i)
            self.zero_lock.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1, 2):
            self.odd_lock.acquire()
            printNumber(i)
            self.zero_lock.release()


def printNumber(n):
    print n

a = ZeroEvenOdd(4)

t1 = threading.Thread(target=a.zero, args=[printNumber])
t2 = threading.Thread(target=a.odd, args=[printNumber])
t3 = threading.Thread(target=a.even, args=[printNumber])
t1.start()
t2.start()
t3.start()