# 1D1P Day107 JUNGOL 1856번 숫자사각형2 문제 - 2021.02.19

n, m = map(int, input().split())

numbers = [[0 for _ in range(m)] for _ in range(n)]

num = 1
for i in range(n):
    for j in range(m):
        if i%2:
            numbers[i][m-1-j] = num
        else:
            numbers[i][j] = num
        
        num += 1

for i in range(n):
    print(*numbers[i])