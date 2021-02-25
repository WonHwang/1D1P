# 1D1P Day113 BOJ 9084번 동전 문제 - 2021.02.25

from sys import stdin
input = stdin.readline

for tc in range(int(input())):
    N = int(input())
    coins = list(map(int, input().rstrip().split()))
    K = int(input())
    dp = [0] * 10001
    dp[0] = 1

    for coin in coins:
        for i in range(1, K+1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]
    
    print(dp[K])