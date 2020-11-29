# 1D1P Day25 BOJ 2407번 조합 문제 - 2020.11.29

n, m = map(int, input().split(' '))

dp = [[0 for _ in range(101)] for __ in range(101)]


for i in range(1, 101):
    for j in range(int(i/2) + 1):
        if j == 0:
            dp[i][j] = 1
            dp[i][i-j] = 1
            continue
        elif j == 1:
            dp[i][j] = i
            dp[i][i-j] = i
            continue
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            dp[i][i-j] = dp[i][j]

print(dp[n][m])