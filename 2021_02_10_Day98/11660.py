# 1D1P Day98 BOJ 11660번 구간 합 구하기 5 문제 - 2021.02.10

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

table = []

for i in range(N):
    table.append(list(map(int, stdin.readline().rstrip().split())))

DP = [[0 for _ in range(N)] for __ in range(N)]

DP[0][0] = table[0][0]
for i in range(1, N):
    DP[i][0] = table[i][0] + DP[i-1][0]
    DP[0][i] = table[0][i] + DP[0][i-1]

for i in range(1, N):
    for j in range(1, N):
        DP[i][j] = table[i][j] + DP[i-1][j] + DP[i][j-1] - DP[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().rstrip().split())
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    if x1 == 0 and y1 == 0:
        answer = DP[x2][y2]
    
    elif x1 == 0:
        answer = DP[x2][y2] - DP[x2][y1 - 1]
    
    elif y1 == 0:
        answer = DP[x2][y2] - DP[x1-1][y2]
    
    else:
        answer = DP[x2][y2] - DP[x1-1][y2] - DP[x2][y1-1] + DP[x1-1][y1-1]
    
    print(answer)