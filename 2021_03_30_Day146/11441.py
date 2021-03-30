# 1D1P Day146 BOJ 11441번 합 구하기 문제 - 2021.03.30

from sys import stdin
input = stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
DP = [0] * N
DP[0] = numbers[0]
for i in range(1, N):
    DP[i] = numbers[i] + DP[i-1]

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a == b:
        print(numbers[a-1])
    else:
        print(DP[b-1]-DP[a-2] if a > 1 else DP[b-1])