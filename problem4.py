import time

palindrome, start_t = 0, time.clock()

for x in range(100, 1000):
    for y in range(x, 1000):
        v = x*y
        sv = str(v)
        if sv == sv[::-1]:
            if v > palindrome:
                palindrome = v

print palindrome
print "time:", time.clock() - start_t, "sec"