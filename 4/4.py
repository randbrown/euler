import sys
import time

start = time.time()

max = 0
for i in range(999, 100, -1):
    for j in range(999, 100, -1):
        val = j * i
        vals = str(val)
        rev = vals[::-1]
        if(rev == vals and val > max):
            max = val

end = time.time()
print("Answer = %d, total elapsed time = %f" % (max, end - start))