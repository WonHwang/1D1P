# 1D1P Day58 BOJ 3184번 양 문제 - 2021.01.01
# Happy New Year!

from sys import stdin
from collections import deque

R, C = map(int, stdin.readline().rstrip().split(' '))
maps = []
for _ in range(R):
    maps.append(stdin.readline().rstrip())

visited = [[0 for _ in range(C)] for __ in range(R)]

def bfs(i, j):
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    wolf = 0
    sheep = 0

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        if maps[x][y] == 'o':
            sheep += 1
        
        elif maps[x][y] == 'v':
            wolf += 1
        
        if x > 0:
            if maps[x-1][y] != '#' and visited[x-1][y] == 0:
                queue.append([x-1, y])
                visited[x-1][y] = 1
        
        if y > 0:
            if maps[x][y-1] != '#' and visited[x][y-1] == 0:
                queue.append([x, y-1])
                visited[x][y-1] = 1
        
        if x < R-1:
            if maps[x+1][y] != '#' and visited[x+1][y] == 0:
                queue.append([x+1, y])
                visited[x+1][y] = 1
        
        if y < C-1:
            if maps[x][y+1] != '#' and visited[x][y+1] == 0:
                queue.append([x, y+1])
                visited[x][y+1] = 1
    
    return sheep, wolf

total_sheep, total_wolf = 0, 0

for i in range(R):
    for j in range(C):
        if visited[i][j] == 0 and maps[i][j] != '#':
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf

print(total_sheep, total_wolf)