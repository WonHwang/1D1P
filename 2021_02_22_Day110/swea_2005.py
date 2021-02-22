# 1D1P Day110 SWEA 2005번 파스칼의 삼각형 문제 - 2021.02.22

DP = [[0 for _ in range(11)] for _ in range(11)]
for i in range(1, 11):
    DP[i][1] = 1
    DP[i][i] = 1

for i in range(3, 11):
    for j in range(2, i+1):
        DP[i][j] = DP[i-1][j] + DP[i-1][j-1]

for tc in range(1, int(input()) + 1):
    N = int(input())
    print(f"#{tc}")
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(DP[i][j], end = ' ')
        print()