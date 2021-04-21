# 1D1P Day168 BOJ 1743번 음식물 피하기 문제 - 2021.04.21

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = 0

def bfs(x, y, N, M):

    global answer

    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    cnt = 0
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        cnt += 1

        for i in range(4):
            a, b = x + dx[i], y + dy[i]

            if 0 <= a < N and 0 <= b < M and maps[a][b] and not visited[a][b]:
                visited[a][b] = 1
                queue.append([a, b])
    
    if cnt > answer:
        answer = cnt

N, M, K = map(int, input().split())

maps = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    maps[r-1][c-1] = 1

visited = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if maps[i][j] and not visited[i][j]:
            bfs(i, j, N, M)

print(answer)