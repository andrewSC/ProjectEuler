def prime_factorization(number):
    factors, divisor = [], 2

    while number > 1:
        while number % divisor == 0:
            factors.append(divisor)  # this is our prime
            number /= divisor
        divisor += 1
    return factors


print prime_factorization(600851475143)
