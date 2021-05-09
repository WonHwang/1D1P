# 1D1P Day186 BOJ 16395번 파스칼의 삼각형 문제 - 2021.05.09

N, K = map(int, input().split())

DP = [[1 for _ in range(31)] for _ in range(31)]

for i in range(1, 31):
    DP[i][1] = i
    DP[i][i-1] = i

for i in range(2, 31):
    for j in range(2, i):
        DP[i][j] = DP[i-1][j-1] + DP[i-1][j]

print(DP[N-1][K-1])