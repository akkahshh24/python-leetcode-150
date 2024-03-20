#Sieve of Erastosthenes
from math import isqrt

def prime_sieve(n: int) -> list[int]:
    # base case
    if n <= 2:
        return []

    # a list to store all the prime numbers
    # for n = 16, make a list of 16 elements [0, 1, 2 ... 15]
    primes = [True] * n
    primes[0] = primes[1] = False

    # for n = 16, sqrt(n) = 4, i = 2, 3
    for i in range(2, isqrt(n)):
        if primes[i]:
            # for i = 2, x = 4, 6, 8, 10, 12, 14
            # for i = 3, x = 9, 12, 15 
            for x in range(i*i, n, i):
                primes[x] = False


    return [i for i in range(n) if primes[i]]

if __name__ == "__main__":
    print(prime_sieve(200))