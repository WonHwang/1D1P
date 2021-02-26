# 1D1P Day114 BOJ 1965번 상자 문제 - 2021.02.26

N = int(input())
box = list(map(int, input().split()))
dp = [1] * N
for i in range(1, N):
    for j in range(0, i):
        if box[j] < box[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))