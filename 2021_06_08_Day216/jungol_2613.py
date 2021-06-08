# 1D1P Day216 JUNGOL 2613번 토마토 문제 - 2021.06.08
# Python에게 TL 1000ms는 가혹해서 안풀리는 문제 억울하다 사이트가 C의 성지라서 그런가. 논리는 문제없고 3000ms 이내로 풀림.

from sys import stdin
from collections import deque
input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())

box = []
for _ in range(N):
    box.append(list(map(int, input().split())))

queue = deque()
visited = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = 1

while queue:
    node = queue.popleft()
    x, y = node[0], node[1]
    day = visited[x][y]

    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if 0 <= a < N and 0 <= b < M and visited[a][b] == 0 and box[a][b] == 0:
            visited[a][b] = day + 1
            box[a][b] = 1
            queue.append([a, b])

for i in range(N):
    for j in range(M):
        if box[i][j] == 0:
            day = -1
            break
    if day == -1:
        break

if day == -1:
    print(day)
else:
    print(day-1)