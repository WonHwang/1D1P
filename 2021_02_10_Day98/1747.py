# 1D1P Day98 BOJ 1747번 소수&팰린드롬 문제 - 2021.02.10

N = int(input())

primes = [1] * 1003002

primes[0] = 0
primes[1] = 0

for i in range(4, 1003002, 2):
    primes[i] = 0

for i in range(3, 1003002, 2):
    if primes[i] == 1:
        for j in range(2*i, 1003002, i):
            primes[j] = 0

for i in range(N, 1003002):
    if primes[i] == 1:
        tmp = str(i)
        if tmp == tmp[::-1]:
            print(i)
            break