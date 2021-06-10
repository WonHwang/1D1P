# 1D1P Day218 BOJ 10810번 공 넣기 문제 - 2021.06.10

from sys import stdin
input = stdin.readline

N, M = map(int, input().split())

basket = [0 for _ in range(N+1)]

for _ in range(M):
    a, b, n = map(int, input().split())

    for i in range(a, b+1):
        basket[i] = n

print(*basket[1:])