# 1D1P Day107 JUNGOL  1338번 문자삼각형1 문제 - 2021.02.19

N = int(input())

table = [[' ' for _ in range(N)] for _ in range(N)]

alpha = 0
for i in range(N):
    for j in range(i, N):
        table[j][N-1-j+i] = chr(alpha + 65)
    
        alpha = (alpha + 1) % 26

for i in range(N):
    print(*table[i])