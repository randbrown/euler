n = 20
prod = 1

def gcd(a, b):
    c = 0
    while (a != 0):
        c = a
        a = b%a
        b = c
    return b

for i in range(1, n+1, 1):
    if prod%i != 0 :
        g = gcd(i, prod)
        prod *= i/g

print("Answer = %d" % (prod))
