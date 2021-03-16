# 1D1P Day132 BOJ 3055번 탈출 문제 - 2021.03.16

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C = map(int, input().rstrip().split())

maps = []
for _ in range(R):
    maps.append(list(input().rstrip()))

queue = deque()
visited = [[0 for _ in range(C)] for _ in range(R)]


for i in range(R):
    for j in range(C):
        if maps[i][j] == '*':
            queue.append([i, j, '*'])
            visited[i][j] = 1

for i in range(R):
    for j in range(C):
        if maps[i][j] == 'S':
            queue.append([i, j, 'S'])

answer = 0

while queue:
    node = queue.popleft()
    x, y, shape = node[0], node[1], node[2]
    step = visited[x][y]
    for i in range(4):
        a, b = x + dx[i], y + dy[i]

        if 0 <= a < R and 0 <= b < C and visited[a][b] == 0 and maps[a][b] == '.':
            visited[a][b] = step + 1
            maps[a][b] = shape
            queue.append([a, b, shape])
        
        elif 0 <= a < R and 0 <= b < C and visited[a][b] == 0 and shape == 'S' and maps[a][b] == 'D':
            answer = step+1
            break
    
    if answer:
        break

print(answer if answer else "KAKTUS")