from sympy import *

num = 600851475143

primeFactorList = []

def getPrimes(limit):

    i = 2

    primeList = []

    while i <= limit :

        if i % 2 == 1 and isprime(i):

            primeList.append(i)

        i += 1

    return primeList

for prime in getPrimes(int(num**0.5)):

    if num % prime == 0:

        primeFactorList.append(prime)

print(max(primeFactorList))

            


        