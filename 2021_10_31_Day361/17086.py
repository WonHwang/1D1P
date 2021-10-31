# 1D1P Day361 BOJ 17086번 아기 상어 2 문제 - 2021.10.31

from sys import stdin
from collections import deque

input = stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1, 1, 1, -1, -1]

N, M = map(int, input().split())
grid = []

for _ in range(N):
    grid.append(list(map(int, input().split())))

step = [[N*M for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            queue = deque()
            visited = [[0 for _ in range(M)] for _ in range(N)]
            queue.append([i, j, 0])
            visited[i][j] = 1

            while queue:
                node = queue.popleft()
                a, b, now = node[0], node[1], node[2]

                if step[a][b] > now:
                    step[a][b] = now
                
                for k in range(8):
                    x, y = a + dx[k], b + dy[k]

                    if 0 <= x < N and 0 <= y < M and not visited[x][y] and not grid[x][y]:
                        visited[x][y] = 1
                        queue.append([x, y, now+1])

answer = 0
for i in range(N):
    for j in range(M):
        if step[i][j] > answer:
            answer = step[i][j]

print(answer)