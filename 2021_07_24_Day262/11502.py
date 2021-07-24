# 1D1P Day262 BOJ 11502번 세 개의 소수 문제 문제 - 2021.07.24

from sys import stdin
input = stdin.readline

sieve = [1] * 1001
sieve[0], sieve[1] = 0, 0
for i in range(4, 1001, 2):
    sieve[i] = 0

for i in range(3, 1001, 2):
    if sieve[i]:
        for j in range(2*i, 1001, i):
            sieve[j] = 0

primes = []

for i in range(1001):
    if sieve[i]:
        primes.append(i)

for _ in range(int(input())):
    N = int(input())

    answer = []
    for a in primes:
        for b in primes:
            for c in primes:
                if a + b + c == N:
                    answer.append(a)
                    answer.append(b)
                    answer.append(c)
                    break
            if answer:
                break
        if answer:
            break
    
    print(*answer if answer else 0)