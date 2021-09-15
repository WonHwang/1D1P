# 1D1P Day315 BOJ 9455번 박스 문제 - 2021.09.15

from sys import stdin
input = stdin.readline

def movetobottom(grid, x, y):

    count = 0
    
    while True:
        if not x or grid[x-1][y]:
            break

        grid[x][y] = 0
        grid[x-1][y] = 1
        x -= 1
        count += 1
    
    return count

for _ in range(int(input())):

    N, M = map(int, input().split())
    grid_tmp = []
    for _ in range(N):
        grid_tmp.append(list(map(int, input().split())))
    
    grid = []
    while grid_tmp:
        grid.append(grid_tmp.pop())
    
    answer = 0

    for i in range(N):
        for j in range(M):
            if i and grid[i][j] and not grid[i-1][j]:
                answer += movetobottom(grid, i, j)

    print(answer)