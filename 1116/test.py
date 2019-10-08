
def outer(a):
    b = 10

    def inner():
        print a + b
    return inner

f = outer(1)
f()
f()
f()
