# 1D1P Day57 BOJ 3187번 양치기 꿍 문제 - 2020.12.31
# 연말연시 행복합시다.

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
    wolf = 0
    sheep = 0
    visited[i][j] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if maps[x][y] == 'v':
            wolf += 1
        elif maps[x][y] == 'k':
            sheep += 1
        
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

answer_sheep = 0
answer_wolf = 0

for i in range(R):
    for j in range(C):
        if maps[i][j] != '#' and visited[i][j] == 0:
            sheep, wolf = bfs(i, j)
            if sheep > wolf:
                answer_sheep += sheep
            else:
                answer_wolf += wolf

print(answer_sheep, answer_wolf)