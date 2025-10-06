from sympy import *

def getPrimesBelowLimit(limit):

    primes = []

    for i in range(limit):

        if isprime(i):

            primes.append(i)

    return primes

print(sum(getPrimesBelowLimit(2000000)))