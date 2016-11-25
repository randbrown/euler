import sys
from sys import argv
import math
import time

start = time.time()

def sieve(n):
    # allocate an extra one to handle the d+n/d max value
    s = [True] * (maxValue+2)
    sq = int(math.sqrt(n))

    for j in range(2, sq+1):
        if s[j] == True:
            for i in range(2*j, n, j):
                s[i] = False
    return s
    
def satisifiesCondition(n):
    if not sieve_array[n+1]:
        return False

    sq = int(math.sqrt(n))

    for i in range(1,sq+1):
        if n%i == 0:
            x = i + n//i
            if sieve_array[x] == False:
                return False
    return True
    
sum = 0
startAt = 1
#maxValue = 100000000
maxValue = 1000

if len(argv) > 1:
    maxValue = int(argv[1])

start_sieve = time.time()
sieve_array = sieve(maxValue)
end_sieve = time.time()
print("finished seive up to %d, elapsed time = %f" % (maxValue, end_sieve - start_sieve))

start_test = time.time()
for i in range(startAt, maxValue+1):
    # print("testing %d" % (i))
    sat = satisifiesCondition(i)
    if(sat):
        # print("{} satisfies condition".format(i))
        sum += i
    
end_test = time.time()
print("Sum = %d, test time = %f, total elapsed time = %f" % (sum, end_test - start_test, end_test - start))
