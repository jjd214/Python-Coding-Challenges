def print_prime_numbers():
    primes = []
    for possiblePrime in range(2, 101):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
        if isPrime:
            primes.append(possiblePrime)
    return primes
print('Prime numbers from 1 to 100')
print(print_prime_numbers())