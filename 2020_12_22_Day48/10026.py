# 1D1P Day48 BOJ 10026번 적록색약 문제 - 2020.12.22

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
grid = []
for _ in range(N):
    grid.append(stdin.readline().rstrip())

visited = [[0 for _ in range(N)] for __ in range(N)]
answer_1 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1
            while queue:
                node = queue.pop()
                x, y = node[0], node[1]
                color = grid[x][y]
                if x > 0:
                    if grid[x-1][y] == color and visited[x-1][y] == 0:
                        queue.append([x-1, y])
                        visited[x-1][y] = 1
                if y > 0:
                    if grid[x][y-1] == color and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                        visited[x][y-1] = 1
                if x < N-1:
                    if grid[x+1][y] == color and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = 1
                if y < N-1:
                    if grid[x][y+1] == color and visited[x][y+1] == 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = 1
            answer_1 += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == 'R':
            grid[i] = grid[i][:j] + 'G' + grid[i][j+1:]

visited = [[0 for _ in range(N)] for __ in range(N)]
answer_2 = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] == 0:
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1
            while queue:
                node = queue.pop()
                x, y = node[0], node[1]
                color = grid[x][y]
                if x > 0:
                    if grid[x-1][y] == color and visited[x-1][y] == 0:
                        queue.append([x-1, y])
                        visited[x-1][y] = 1
                if y > 0:
                    if grid[x][y-1] == color and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                        visited[x][y-1] = 1
                if x < N-1:
                    if grid[x+1][y] == color and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = 1
                if y < N-1:
                    if grid[x][y+1] == color and visited[x][y+1] == 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = 1
            answer_2 += 1

print(answer_1, answer_2)