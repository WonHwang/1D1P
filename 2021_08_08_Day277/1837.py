# 1D1P Day277 BOJ 1837번 암호제작 문제 - 2021.08.08

primes = [1] * 1000001
primes[0], primes[1] = 0, 0
for i in range(4, 1000001, 2):
    primes[i] = 0

for i in range(3, 1000001, 2):
    if primes[i]:
        for j in range(2*i, 1000001, i):
            primes[j] = 0

P, K = map(int, input().split())

for i in range(2, K):
    if primes[i] and not P%i:
        print(f"BAD {i}")
        break
else:
    print('GOOD')