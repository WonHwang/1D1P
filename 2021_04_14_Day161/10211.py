# 1D1P Day161 BOJ 10211번 Maximum Subarray 문제 - 2021.04.14

from sys import stdin
input = stdin.readline


for tc in range(int(input())):

    N = int(input())
    numbers = list(map(int, input().rstrip().split()))

    dp = [0] * N
    dp[0] = numbers[0]

    for i in range(1, N):
        dp[i] = max(dp[i-1] + numbers[i], numbers[i])
    
    print(max(dp))