# 1D1P Day163 BOJ 12865번 평범한 배낭 문제 - 2021.04.16

from sys import stdin
input = stdin.readline

N, K = map(int, input().rstrip().split())

weights = [0]
values = [0]

for _ in range(N):
    a, b = map(int, input().rstrip().split())
    weights.append(a)
    values.append(b)

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):

        if weights[i] <= j:
            dp[i][j] = max(values[i] + dp[i-1][j-weights[i]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])