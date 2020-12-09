# 1D1P Day35 BOJ 7569번 토마토 문제 - 2020.12.09

from sys import stdin
from collections import deque

M, N, H = map(int, stdin.readline().rstrip().split(' '))

tomato = []

for h in range(H):
    tmp = []
    for n in range(N):
        tmp.append(stdin.readline().rstrip().split(' '))
    tomato.append(tmp)

visited = [[[-1 for _ in range(M)] for __ in range(N)]  for ___ in range(H)]

def check():
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomato[h][n][m] == '0':
                    return False
    
    return True

queue = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == '1':
                queue.append([h, n, m, 0])
                visited[h][n][m] == 0

while queue:
    node = queue.popleft()
    h, n, m, day = node[0], node[1], node[2], node[3]
    tomato[h][n][m] = '1'

    if h < H-1 and tomato[h+1][n][m] == '0' and visited[h+1][n][m] == -1:
        queue.append([h+1, n, m, day + 1])
        visited[h+1][n][m] = day + 1
    
    if h > 0 and tomato[h-1][n][m] == '0' and visited[h-1][n][m] == -1:
        queue.append([h-1, n, m, day + 1])
        visited[h-1][n][m] = day + 1
    
    if n < N-1 and tomato[h][n+1][m] == '0' and visited[h][n+1][m] == -1:
        queue.append([h, n+1, m, day + 1])
        visited[h][n+1][m] = day + 1
    
    if n > 0 and tomato[h][n-1][m] == '0' and visited[h][n-1][m] == -1:
        queue.append([h, n-1, m, day + 1])
        visited[h][n-1][m] = day + 1

    if m < M-1 and tomato[h][n][m+1] == '0' and visited[h][n][m+1] == -1:
        queue.append([h, n, m+1, day + 1])
        visited[h][n][m+1] = day + 1
    
    if m > 0 and tomato[h][n][m-1] == '0' and visited[h][n][m-1] == -1:
        queue.append([h, n, m-1, day + 1])
        visited[h][n][m-1] = day + 1

if check():
    answer = 0
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if visited[h][n][m] > answer:
                    answer = visited[h][n][m]
    
    print(answer)

else:
    print(-1)