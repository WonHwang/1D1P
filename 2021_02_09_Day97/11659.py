# 1D1P Day97 BOJ 11659번 구간 합 구하기 4 문제 - 2021.02.09

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())
numbers = list(map(int,stdin.readline().rstrip().split()))
DP = [0] * N

DP[0] = numbers[0]
for i in range(1, N):
    DP[i] = DP[i-1] + numbers[i]
    
for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split())
    if a == 1:
        print(DP[b-1])
    else:
        print(DP[b-1] - DP[a-2])