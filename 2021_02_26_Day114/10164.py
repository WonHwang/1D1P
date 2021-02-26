# 1D1P Day114 BOJ 10164번 격자상의 경로 문제 - 2021.02.26

N, M, K = map(int, input().split())

if K % M == 0:
    x = (K // M) - 1
    y = M-1

else:
    x = K // M
    y = (K % M) - 1

dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1

for i in range(x+1):
    for j in range(y+1):
        if i == 0 and j == 0:
            continue
        t, l = 0, 0
        if i > 0:
            t = dp[i-1][j]
        if j > 0:
            l = dp[i][j-1]
        dp[i][j] = t + l

if K == 0:
    x, y = 0, 0

for i in range(x, N):
    for j in range(y, M):
        if i == 0 and j == 0:
            continue
        t, l = 0, 0
        if i > 0:
            t = dp[i-1][j]
        if j > 0:
            l = dp[i][j-1]
        dp[i][j] = t + l

print(dp[N-1][M-1])