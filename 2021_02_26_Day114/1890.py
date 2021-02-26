# 1D1P Day114 BOJ 1890번 점프 문제 - 2021.02.26

from sys import stdin
input = stdin.readline

N = int(input())

numbers = []
for _ in range(N):
    numbers.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        tmp = numbers[i][j]
        if i + tmp < N and dp[i][j] != 0:
            dp[i+tmp][j] += dp[i][j]
        if j + tmp < N and dp[i][j] != 0:
            dp[i][j+tmp] += dp[i][j]

print(dp[N-1][N-1])