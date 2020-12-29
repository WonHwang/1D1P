# 1D1P Day55 BOJ 16948번 데스 나이트 문제 - 2020.12.29

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
r1, c1, r2, c2 = map(int, stdin.readline().rstrip().split(' '))

visited = [[0 for _ in range(N)] for __ in range(N)]

queue = deque()
queue.append([r1, c1])
visited[r1][c1] = 1
answer = -1

while queue:
    node = queue.popleft()
    x, y = node[0], node[1]
    step = visited[x][y]

    if x == r2 and y == c2:
        answer = visited[r2][c2] - 1
        break
    
    if x >= 2 and y >= 1:
        if visited[x-2][y-1] == 0:
            queue.append([x-2, y-1])
            visited[x-2][y-1] = step + 1
    
    if y >= 2:
        if visited[x][y-2] == 0:
            queue.append([x, y-2])
            visited[x][y-2] = step + 1
    
    if x <= N-3 and y >= 1:
        if visited[x+2][y-1] == 0:
            queue.append([x+2, y-1])
            visited[x+2][y-1] = step + 1
    
    if x <= N-3 and y <= N-2:
        if visited[x+2][y+1] == 0:
            queue.append([x+2, y+1])
            visited[x+2][y+1] = step + 1
    
    if y <= N-3:
        if visited[x][y+2] == 0:
            queue.append([x, y+2])
            visited[x][y+2] = step + 1
    
    if x >= 2 and y <= N-2:
        if visited[x-2][y+1] == 0:
            queue.append([x-2, y+1])
            visited[x-2][y+1] = step + 1

print(answer)