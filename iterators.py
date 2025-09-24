# iterator and generators -useful for streaming-
def fib(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b, a+b

for x in fib(10):
    print(x)



# Decorator example:

import time
def timeit(fn):
    def wrapped(*a, **kw):
        t0 = time.time()
        res = fn(*a, **kw)
        print("time:", time.time()-t0)
        return res
    return wrapped

@timeit
def slow():
    sum(range(1000000))
slow()