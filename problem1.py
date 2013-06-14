def find_sum_of_multiples(max_sum):
    sum, x, y = (0, 1, 1)
    t1 = lambda x: 3*x
    t2 = lambda y: 5*y

    while t1(x) < max_sum or t2(y) < max_sum:
        if t1(x) < t2(y):
            sum += t1(x)
            x += 1
        elif t2(y) < t1(x):
            sum += t2(y)
            y += 1
        else:
            sum += t1(x)  # we're just picking one because t1 and t2 and equal
            x += 1
            y += 1  # and we're incrementing both because we don't want repeats to be summed
    return sum

print find_sum_of_multiples(1000)