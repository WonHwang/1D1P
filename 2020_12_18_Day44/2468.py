# 1D1P Day44 BOJ 2468번 안전 영역 문제 - 2020.12.18

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())

area = []

for _ in range(N):
    area.append(stdin.readline().rstrip().split(' '))

maximum = 0
for i in range(N):
    for j in range(N):
        area[i][j] = int(area[i][j])
        if area[i][j] > maximum:
            maximum = area[i][j]

answer = 0
for h in range(maximum + 1):
    visited = [[0 for _ in range(N)] for __ in range(N)]
    result = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] - h > 0 and visited[i][j] == 0:
                queue = deque()
                queue.append([i, j])
                visited[i][j] = 1
                while queue:
                    node = queue.popleft()
                    x = node[0]
                    y = node[1]

                    if x < N-1:
                        if area[x+1][y] - h > 0 and visited[x+1][y] == 0:
                            queue.append([x+1, y])
                            visited[x+1][y] = 1
                    if y < N-1:
                        if area[x][y+1] - h > 0 and visited[x][y+1] == 0:
                            queue.append([x, y+1])
                            visited[x][y+1] = 1
                    if x > 0:
                        if area[x-1][y] - h > 0 and visited[x-1][y] == 0:
                            queue.append([x-1, y])
                            visited[x-1][y] = 1
                    if y > 0:
                        if area[x][y-1] - h > 0 and visited[x][y-1] == 0:
                            queue.append([x, y-1])
                            visited[x][y-1] = 1
                result += 1
    if result > answer:
        answer = result

print(answer)