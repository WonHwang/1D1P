# 1D1P Day25 BOJ 2583번 영역 구하기 문제 - 2020.11.29

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().rstrip().split(' '))

paper = [[0 for _ in range(N+1)] for __ in range(M+1)]
visited = [[0 for _ in range(N+1)] for __ in range(M+1)]

for _ in range(K):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split(' '))
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

areas = []
for i in range(M):
    for j in range(N):
        area = 0
        if paper[i][j] == 0 and visited[i][j] == 0:
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1
            while queue:
                node = queue.popleft()
                area += 1
                x = node[0]
                y = node[1]
                if paper[x+1][y] == 0 and visited[x+1][y] == 0 and x+1 < M:
                    queue.append([x+1, y])
                    visited[x+1][y] = 1
                if paper[x][y+1] == 0 and visited[x][y+1] == 0 and y+1 < N:
                    queue.append([x, y+1])
                    visited[x][y+1] = 1
                if paper[x-1][y] == 0 and visited[x-1][y] == 0 and x-1 >= 0:
                    queue.append([x-1, y])
                    visited[x-1][y] = 1
                if paper[x][y-1] == 0 and visited[x][y-1] == 0 and y-1 >= 0:
                    queue.append([x, y-1])
                    visited[x][y-1] = 1
            areas.append(area)

areas.sort()
print(len(areas))
answer = ""
for _ in areas:
    answer += str(_) + " "

print(answer[:-1])