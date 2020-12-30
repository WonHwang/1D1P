# 1D1P Day56 BOJ 14716번 현수막 문제 - 2020.12.30

from sys import stdin
from collections import deque

M, N = map(int, stdin.readline().rstrip().split(' '))

maps = []

for _ in range(M):
    maps.append(stdin.readline().rstrip().split(' '))

visited = [[0 for _ in range(N)] for __ in range(M)]

answer = 0
for i in range(M):
    for j in range(N):
        if maps[i][j] == '1' and visited[i][j] == 0:
            queue = deque()
            queue.append([i, j])
            visited[i][j] = 1

            while queue:
                node = queue.popleft()
                x, y = node[0], node[1]

                if x > 0:
                    if maps[x-1][y] == '1' and visited[x-1][y] == 0:
                        queue.append([x-1, y])
                        visited[x-1][y] = 1
                
                if y > 0:
                    if maps[x][y-1] == '1' and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                        visited[x][y-1] = 1

                if x < M-1:
                    if maps[x+1][y] == '1' and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = 1
                
                if y < N-1:
                    if maps[x][y+1] == '1' and visited[x][y+1] == 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = 1
                
                if x > 0 and y > 0:
                    if maps[x-1][y-1] == '1' and visited[x-1][y-1] == 0:
                        queue.append([x-1, y-1])
                        visited[x-1][y-1] = 1
                
                if x > 0 and y < N-1:
                    if maps[x-1][y+1] == '1' and visited[x-1][y+1] == 0:
                        queue.append([x-1, y+1])
                        visited[x-1][y+1] = 1
                
                if x < M-1 and y > 0:
                    if maps[x+1][y-1] == '1' and visited[x+1][y-1] == 0:
                        queue.append([x+1, y-1])
                        visited[x+1][y-1] = 1
                
                if x < M-1 and y < N-1:
                    if maps[x+1][y+1] == '1' and visited[x+1][y+1] == 0:
                        queue.append([x+1, y+1])
                        visited[x+1][y+1] = 1
            
            answer += 1

print(answer)