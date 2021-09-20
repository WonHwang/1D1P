# 1D1P Day320 BOJ 13301번 타일 장식물 문제 - 2021.09.20

DP = [0] * 82
DP[0] = DP[1] = 1
N = int(input())

for i in range(2, N+1):
    DP[i] = DP[i-1] + DP[i-2]

print(2*(DP[N] + DP[N-1]))