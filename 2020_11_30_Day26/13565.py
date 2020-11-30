# 1D1P Day26 BOJ 13565번 침투 문제 - 2020.11.30

from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().rstrip().split(' '))

square = [['1' for _ in range(N+2)] for __ in range(M+2)]

for i in range(1, M+1):
    line = stdin.readline().rstrip()
    for j in range(1, N+1):
        square[i][j] = line[j-1]

visited = [[0 for _ in range(N+2)] for __ in range(M+2)]

for i in range(N):
    queue = deque()
    result = 0
    if square[1][i] == '0' and visited[1][i] == 0:
        queue.append([0, i])
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if x == M:
            result = 1
            break
        if square[x+1][y] == '0' and visited[x+1][y] == 0 and x+1 <= M :
            queue.append([x+1, y])
            visited[x+1][y] = 1
        if square[x][y+1] == '0' and visited[x][y+1] == 0 and y+1 <= N:
            queue.append([x, y+1])
            visited[x][y+1] = 1
        if square[x-1][y] == '0' and visited[x-1][y] == 0 and x-1 >= 0:
            queue.append([x-1, y])
            visited[x-1][y] = 1
        if square[x][y-1] == '0' and visited[x][y-1] == 0 and y-1 >= 0:
            queue.append([x, y-1])
            visited[x][y-1]
    if result == 1:
        break

if result:
    print("YES")
else:
    print("NO")