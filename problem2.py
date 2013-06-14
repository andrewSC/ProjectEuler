a, b, sum = 1, 2, 0

while a < 4000000:
    a, b = b, a+b
    sum += a if not a % 2 else 0

print sum
