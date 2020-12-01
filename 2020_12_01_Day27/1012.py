# 1D1P Day27 BOJ 1012번 유기농 배추 문제 - 2020.12.01

from sys import stdin
from collections import deque

T = int(stdin.readline().rstrip())
for __ in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split(' '))
    field = [[0 for _ in range(M+2)] for ___ in range(N+2)]
    visited = [[0 for _ in range(M+2)] for ___ in range(N+2)]

    for _ in range(K):
        x, y = map(int, stdin.readline().rstrip().split(' '))
        field[y+1][x+1] = 1
    
    answer = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if field[i][j] == 1 and visited[i][j] == 0:
                queue = deque()
                queue.append([i, j])
                visited[i][j] = 1
                while queue:
                    node = queue.popleft()
                    x, y = node[0], node[1]
                    if field[x+1][y] == 1 and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = 1
                    if field[x][y+1] == 1 and visited[x][y+1] == 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = 1
                    if field[x-1][y] == 1 and visited[x-1][y] == 0:
                        queue.append([x-1, y])
                        visited[x-1][y] = 1
                    if field[x][y-1] == 1 and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                        visited[x][y-1] = 1
                answer += 1
    
    print(answer)