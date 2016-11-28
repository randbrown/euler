n = 20
prod = 1

# first do a crude guess
for i in range(n,1, -1):
    if prod%i != 0:
        prod *= i

# then reduce if possible
for i in range(n,1, -1):
    test = prod/i
    canDivByThis = True
    for j in range(n,1,-1) :
        if test%j != 0:
            canDivByThis = False
            break
    if canDivByThis:
        prod = test

print("Answer = %d" % (prod))

    