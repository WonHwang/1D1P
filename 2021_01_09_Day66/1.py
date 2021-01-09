from sys import stdin
import copy

primes = dict()

primes[2] = 0
for i in range(3, 100001):

    result = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            result = False
            break
    if result:
        primes[i] = 0

def factorization(N, primes):
    for key in primes:
        if N % key == 0:
            tmp = 0
            while N % key == 0:
                tmp += 1
                N = N // key
            primes[key] = tmp
        if N == 1:
            break
    
    return primes

T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    tmp = copy.deepcopy(primes)
    result = factorization(N, tmp)

    for key in result:
        if result[key] != 0:
            print(key, result[key])