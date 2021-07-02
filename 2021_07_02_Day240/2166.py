# 1D1P Day240 BOJ 2166번 다각형의 면적 문제 - 2021.07.02

from sys import stdin
input = stdin.readline

N = int(input())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))
grid.append(grid[0])

tmp1 = 0
for i in range(N):
    tmp1 += grid[i][0] * grid[i+1][1]

tmp2 = 0
for i in range(N):
    tmp2 += grid[i][1] * grid[i+1][0]

answer = abs(tmp1 - tmp2) / 2
print(round(answer, 1))