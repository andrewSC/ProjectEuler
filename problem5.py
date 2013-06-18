import time

start_t, found, smallest_number, divisors = time.clock(), 0, 1, range(2, 21)

while not found:
    for divisor in divisors:
        if smallest_number % divisor == 0:
            if divisor == 20:
                print smallest_number
                found = 1
                break
        else:
            break
    smallest_number += 1


print "Elapsed time:", time.clock() - start_t, "sec"



'''
Also could do it with set intersection but it's pretty gross. :((
'''
# lcm = []
# for x in range(2, 21):
#     lcm.append(range(x, 250000000, x))
# print reduce(set.intersection, map(set, lcm))
