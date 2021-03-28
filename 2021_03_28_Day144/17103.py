# 1D1P Day144 BOJ 17103번 골드바흐 파티션 문제 - 2021.03.28

from sys import stdin
input = stdin.readline

primes = [1] * 1000001

primes[0] = 0
primes[1] = 0

for i in range(4, 1000001, 2):
    primes[i] = 0

for i in range(3, 1000001, 2):
    if primes[i] == 1:
        for j in range(2*i, 1000001, i):
            primes[j] = 0

for _ in range(int(input())):
    N = int(input())
    
    cnt = 0
    for i in range(2, N//2 + 1):
        if primes[i] and primes[N-i]:
            cnt += 1
    
    print(cnt)