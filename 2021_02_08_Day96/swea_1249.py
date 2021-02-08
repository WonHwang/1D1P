# 1D1P Day96 SWEA 1249번 보급로 문제 - 2021.02.08

from collections import deque

for t in range(1, int(input()) + 1):
    N = int(input())
    maps = []
    for i in range(N):
        maps.append(input())
    visited = [[0 for _ in range(N)] for __ in range(N)]
    queue = deque()
    queue.append([0, 0])
    visited[0][0] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        step = visited[x][y]

        if x > 0:
            if visited[x-1][y] == 0 or visited[x-1][y] > step + int(maps[x-1][y]):
                queue.append([x-1, y])
                visited[x-1][y] = step + int(maps[x-1][y])
        
        if y > 0:
            if visited[x][y-1] == 0 or visited[x][y-1] > step + int(maps[x][y-1]):
                queue.append([x, y-1])
                visited[x][y-1] = step + int(maps[x][y-1])
        
        if x < N-1:
            if visited[x+1][y] == 0 or visited[x+1][y] > step + int(maps[x+1][y]):
                queue.append([x+1, y])
                visited[x+1][y] = step + int(maps[x+1][y])
        if y < N-1:
            if visited[x][y+1] == 0 or visited[x][y+1] > step + int(maps[x][y+1]):
                queue.append([x, y+1])
                visited[x][y+1] = step + int(maps[x][y+1])
    
    print(f"#{t} {visited[N-1][N-1] - 1}")