# 1D1P Day113 BOJ 2294번 동전 2 문제 - 2021.02.25

N, K = map(int, input().split())
coins = []

for _ in range(N):
    coins.append(int(input()))
coins.sort()

dp = [0] * 100001
for coin in coins:
    dp[coin] = 1
for coin in coins:
    for i in range(1, K+1):
        if i - coin > 0:
            if dp[i] == 0:
                if dp[i-coin] != 0:
                    dp[i] = dp[i-coin] + 1
            else:
                if dp[i-coin] != 0:
                    dp[i] = min(dp[i-coin] + 1, dp[i])

print(dp[K] if dp[K] else -1)