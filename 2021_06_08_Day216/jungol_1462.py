# 1D1P Day216 JUNGOL 1462번 보물섬 문제 - 2021.06.08
# Unsolved!

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

grid = []

for _ in range(N):
    grid.append(input().rstrip())

visited = [[0 for _ in range(M)] for _ in range(N)]

def bfs(sx, sy, N, M):

    queue = deque()

    queue.append([sx, sy])
    visited[sx][sy] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        step = visited[x][y]

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if 0 <= a < N and 0 <= b < M and visited[a][b] == 0 and grid[a][b] == 'L':
                visited[a][b] = step + 1
                queue.append([a, b])

    Max = 0
    ex, ey = -1, -1
    for i in range(N):
        for j in range(M):
            if visited[i][j] > Max:
                Max = visited[i][j]
                ex, ey = i, j
    
    return ex, ey, Max

answer = 0

for i in range(N):
    for j in range(M):
        if grid[i][j] == 'L' and visited[i][j] == 0:
            ex, ey, tmpMax = bfs(i, j, N, M)
            new_visited = [[0 for _ in range(M)] for _ in range(N)]
            queue = deque()
            queue.append([ex, ey])
            new_visited[ex][ey] = 1

            while queue:
                node = queue.popleft()
                x, y = node[0], node[1]
                step = new_visited[x][y]

                for k in range(4):
                    a, b = x + dx[k], y + dy[k]
                    if 0 <= a < N and 0 <= b < M and new_visited[a][b] == 0 and grid[a][b] == 'L':
                        new_visited[a][b] = step + 1
                        queue.append([a, b])
            
            Max = 0
            for k in range(N):
                for l in range(M):
                    if new_visited[k][l] > Max:
                        Max = new_visited[k][l]
            
            if Max > answer:
                answer = Max

print(answer-1)