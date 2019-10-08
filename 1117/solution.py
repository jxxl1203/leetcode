import threading
class H2O(object):
    sema_h = threading.Semaphore
    sema_o = threading.Semaphore
    lock = threading.Lock
    def __init__(self):
        self.sema_h = threading.Semaphore(2)
        self.sema_o = threading.Semaphore(0)
        self.lock = threading.Lock()
    def hydrogen(self, releaseHydrogen):
        """
        :type releaseHydrogen: method
        :rtype: void
        """

        # releaseHydrogen() outputs "H". Do not change or remove this line.
        self.sema_h.acquire()
        releaseHydrogen()
        self.sema_o.release()


    def oxygen(self, releaseOxygen):
        """
        :type releaseOxygen: method
        :rtype: void
        """
        self.lock.acquire(True)
        self.sema_o.acquire()
        self.sema_o.acquire()
        self.lock.release()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.sema_h.release()
        self.sema_h.release()


def releaseOxygen():
    print "O"

def releaseHydrogen():
    print "H"

a = H2O()
# s = "OHOHOOHHOHHOOHHHHOOHOOHHOHHOOHHHOOHOHHOHHOHHHHHOHHHHHHHHHHHH"
s = "OOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHHOOOOOOOOOOHHHHHHHHHHHHHHHHHHHH"
for i in s:
    if i == "H":
        threading.Thread(target=a.hydrogen, args=[releaseHydrogen]).start()
    else:
        threading.Thread(target=a.oxygen, args=[releaseOxygen]).start()

# threading.Thread(target=a.hydrogen, args=[releaseHydrogen]).start()
# threading.Thread(target=a.hydrogen, args=[releaseHydrogen]).start()
# threading.Thread(target=a.hydrogen, args=[releaseHydrogen]).start()
# threading.Thread(target=a.oxygen, args=[releaseOxygen]).start()



