# 1D1P Day257 BOJ 18405번 경쟁적 감염 문제 - 2021.07.19

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, K = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

S, X, Y = map(int, input().split())

visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()

target = []
for i in range(N):
    for j in range(N):
        if grid[i][j]:
            visited[i][j] = 1
            target.append([grid[i][j], i, j, 0])

target.sort(key=lambda x:x[0])

for node in target:
    queue.append(node)

while queue:
    node = queue.popleft()
    num, x, y, time = node[0], node[1], node[2], node[3]
    if time > S:
        break
    grid[x][y] = num

    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < N and not visited[a][b]:
            visited[a][b] = 1
            queue.append([num, a, b, time+1])

print(grid[X-1][Y-1])