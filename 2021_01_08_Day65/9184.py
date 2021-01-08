# 1D1P Day65 BOJ 9184번 신나는 함수 실행 문제 - 2021.01.08

import sys

input = sys.stdin.readline

DP = dict()

for i in range(-50, 51):
    DP[i] = dict()
    for j in range(-50, 51):
        DP[i][j] = dict()
        for k in range(-50, 51):

            if i <= 0 or j <= 0 or k <= 0:
                DP[i][j][k] = 1
            
            elif i > 20 or j > 20 or k > 20:
                DP[i][j][k] = 1048576 # 미리 계산했습니다.
            
            elif i < j and j < k:
                DP[i][j][k] = DP[i][j][k-1] + DP[i][j-1][k-1] - DP[i][j-1][k]
            
            else:
                DP[i][j][k] = DP[i-1][j][k] + DP[i-1][j-1][k] + DP[i-1][j][k-1] - DP[i-1][j-1][k-1]

while True:
    a, b, c = map(int, input().split(' '))
    if a == -1 and b == -1 and c == -1:
        break
    print("w(%d, %d, %d) = %d" %(a, b, c, DP[a][b][c]))