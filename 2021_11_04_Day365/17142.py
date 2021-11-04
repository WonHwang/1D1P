# 1D1P Day365 BOJ 17142锅 楷备家 3 巩力 - 2021.11.04
# 1林斥!

from collections import deque
from itertools import combinations

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

viruses = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == 2:
            viruses.append([i, j])

target = list(combinations(viruses, M))
answer = (N**2) + 1

for virus in target:
    queue = deque()
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M):
        queue.append(virus[i])
        visited[virus[i][0]][virus[i][1]] = 1
    
    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        time = visited[a][b]

        for i in range(4):
            x, y = a + dx[i], b + dy[i]
            if 0 <= x < N and 0 <= y < N and not visited[x][y] and grid[x][y] != 1:
                visited[x][y] = time + 1
                queue.append([x, y])
    
    Max = 1
    for i in range(N):
        for j in range(N):
            if grid[i][j] != 2 and visited[i][j] > Max:
                Max = visited[i][j]
            if grid[i][j] == 0 and not visited[i][j]:
                Max = -1
                break
        if Max == -1:
            break
    
    if Max != -1 and Max < answer:
        answer = Max

if answer == (N**2) + 1:
    answer = -1

print(answer-1 if answer != -1 else answer)