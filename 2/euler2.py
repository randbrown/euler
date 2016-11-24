import sys
import functools

######### approach 1 (crude, inefficient)
# cache results makes it much faster
@functools.lru_cache(maxsize=None)
def fib(n):
    if(n <= 1):
        return 1
    if(n == 2):
        return 2
    return fib(n-1) + fib(n-2)

# works but not efficient at all
def fibsum0(n):
    idx=0
    f = 0
    sum = 0
    while(f < n):
        f = fib(idx)
        if(f % 2 == 0):
            sum = sum + f
        idx = idx+1
    return sum

arg = 10
if(len(sys.argv) > 1):
    arg = int(sys.argv[1])
answer = fibsum0(arg)
print("sum (using simple approach) = {}".format(answer))

########## approach 2, much more efficient
def fibsum(n):
    g=0
    f=1
    sum = 0
    ##### THIS IS NOT RIGHT
    while(f<n):
        print("fib number: %d" % f)
        if(f%2 == 0):
            print("adding even number: %d" % f)
            sum += f
        temp = f
        f += g
        g = temp
    return sum

answer = fibsum(arg)
print("sum (better method) = {}".format(answer))