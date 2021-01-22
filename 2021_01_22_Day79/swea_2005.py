# 1D1P Day79 SWEA 2005번 파스칼의 삼각형 문제 - 2021.01.22

T = int(input())
for _ in range(T):
    N = int(input())
    DP = [[1 for i in range(N+1)] for j in range(N+1)]
    for i in range(3, N+1):
        for j in range(2, i):
            DP[i][j] = DP[i-1][j-1] + DP[i-1][j]
    print(f"#{_+1}")
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(DP[i][j], end=' ')
        print()