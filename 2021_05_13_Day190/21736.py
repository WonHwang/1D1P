# 1D1P Day190 BOJ 21736번 헌내기는 친구가 필요해 문제 - 2021.05.13

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())

maps = []
for _ in range(N):
    maps.append(input().rstrip())

start = []
for i in range(N):
    for j in range(M):
        if maps[i][j] == 'I':
            start = [i, j]
            break
    
    if start:
        break

queue = deque()
queue.append(start)
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[start[0]][start[1]] = 1

answer = 0
while queue:
    node = queue.popleft()
    x, y = node[0], node[1]

    if maps[x][y] == 'P':
        answer += 1

    for i in range(4):
        a, b = x + dx[i], y + dy[i]

        if 0 <= a < N and 0 <= b < M and visited[a][b] == 0 and maps[a][b] != 'X':
            visited[a][b] = 1
            queue.append([a, b])

print(answer if answer else 'TT')