# 1D1P Day20 BOJ 2178번 미로 탐색 문제 - 2020.11.24

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

maze = [[0 for _ in range(M+2)] for __ in range(N+2)]
visited = [[N*M for _ in range(M+2)] for __ in range(N+2)]

for i in range(N):
    input_ = sys.stdin.readline().rstrip()
    for j in range(M):
        maze[i+1][j+1] = int(input_[j])

def dfs(i, j):
    
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if maze[x+1][y] == 1 and visited[x+1][y] > visited[x][y] + 1:
            queue.append([x+1, y])
            visited[x+1][y] = visited[x][y] + 1
        if maze[x][y+1] == 1 and visited[x][y+1] > visited[x][y] + 1:
            queue.append([x, y+1])
            visited[x][y+1] = visited[x][y] + 1
        if maze[x-1][y] == 1 and visited[x-1][y] > visited[x][y] + 1:
            queue.append([x-1, y])
            visited[x-1][y] = visited[x][y] + 1
        if maze[x][y-1] == 1 and visited[x][y-1] > visited[x][y] + 1:
            queue.append([x, y-1])
            visited[x][y-1] = visited[x][y] + 1

dfs(1, 1)

print(visited[N][M])