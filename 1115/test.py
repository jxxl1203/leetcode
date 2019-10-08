import threading
import time

def a():
    while True:
        lockb.acquire()
        print('a')
        locka.release()
        time.sleep(0.5)


def b():
    while True:
        locka.acquire()
        print('b')
        lockb.release()
        time.sleep(0.5)


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()

    ta = threading.Thread(target=a)
    tb = threading.Thread(target=b)

    locka.acquire()

    ta.start()
    tb.start()
