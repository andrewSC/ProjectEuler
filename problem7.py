import time
import math
# import numpypy  # for pypy, apparently
import numpy

start_t = time.clock()
lim = 500000  # arbitrary limit
sieve = numpy.zeros(lim+1, dtype=numpy.bool)
sqrt_lim = int(math.sqrt(lim))

def comp(n):
    count = 1
    last = count*n**2
    c = []
    while last <= lim:
        c.append(last)
        count += 1
        last = count*n**2
    return c

for x in xrange(1, sqrt_lim):
    for y in xrange(1, sqrt_lim):

        n = 4*x**2 + y**2
        if n <= lim and (n % 12 == 1 or n % 12 == 5):
            sieve[n] = not sieve[n]

        n = 3*x**2 + y**2
        if n <= lim and n % 12 == 7:
            sieve[n] = not sieve[n]

        n = 3*x**2 - y**2
        if (x > y) and n <= lim and n % 12 == 11:
            sieve[n] = not sieve[n]


for x in xrange(5, sqrt_lim):
    if sieve[x]:
        for k in comp(x):
            sieve[k] = False

prime_count = 2  # Starting at two because we're not including primes 2 and 3 in the output/computation
for n in xrange(0, lim):  # Now we go through the boolean array and find our 10,001st prime
    if sieve[n]:
        prime_count += 1
        if prime_count == 10001:
            print n
            break

print prime_count
print "time:", time.clock() - start_t, "sec"
