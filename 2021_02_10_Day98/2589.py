# 1D1P Day98 BOJ 2589번 보물섬 문제 - 2021.02.10

from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().rstrip().split())
maps = []
for i in range(H):
    maps.append(list(stdin.readline().rstrip()))

DP = [[0 for _ in range(W)] for __ in range(H)]

def bfs(a, b):
    visited = [[0 for _ in range(W)] for __ in range(H)]
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        step = visited[x][y]

        if x > 0 and visited[x-1][y] == 0 and maps[x-1][y] == 'L':
            queue.append([x-1, y])
            visited[x-1][y] = step + 1
        
        if y > 0 and visited[x][y-1] == 0 and maps[x][y-1] == 'L':
            queue.append([x, y-1])
            visited[x][y-1] = step + 1
        
        if x < H-1 and visited[x+1][y] == 0 and maps[x+1][y] == 'L':
            queue.append([x+1, y])
            visited[x+1][y] = step + 1
        
        if y < W-1 and visited[x][y+1] == 0 and maps[x][y+1] == 'L':
            queue.append([x, y+1])
            visited[x][y+1] = step + 1
    
    answer = max(visited[0])
    for i in range(1, H):
        if max(visited[i]) > answer:
            answer = max(visited[i])
    
    DP[a][b] = answer - 1

for i in range(H):
    for j in range(W):
        if maps[i][j] == 'L':
            bfs(i, j)

answer = max(DP[0])
for i in range(1, H):
    if max(DP[i]) > answer:
        answer = max(DP[i])

print(answer)