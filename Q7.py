def isPrime(num):
    
    if num == 0: return False
    
    sqr = int(num**0.5)

    for i in range(2,sqr + 1):

        if num % i == 0:return False

    return True

primes = 0
num = -1

while primes != 10002:
    
    num += 1

    if isPrime(num): primes += 1

print(num)
    