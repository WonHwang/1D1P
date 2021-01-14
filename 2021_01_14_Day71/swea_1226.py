# 1D1P Day71 SWEA 1226번 [S/W 문제해결 기본] 7일차 - 미로1 문제 - 2021.01.14

from collections import deque

for _ in range(10):

    t = int(input())
    maze = []
    for i in range(16):
        maze.append(input())
    visited = [[0 for i in range(16)] for j in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start = [i, j]
            elif maze[i][j] == '3':
                end = [i, j]
    
    x, y = start[0], start[1]
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        
        if maze[x+1][y] != '1' and visited[x+1][y] == 0:
            queue.append([x+1, y])
            visited[x+1][y] = 1
        
        if maze[x-1][y] != '1' and visited[x-1][y] == 0:
            queue.append([x-1, y])
            visited[x-1][y] = 1
        
        if maze[x][y+1] != '1' and visited[x][y+1] == 0:
            queue.append([x, y+1])
            visited[x][y+1] = 1
        
        if maze[x][y-1] != '1' and visited[x][y-1] == 0:
            queue.append([x, y-1])
            visited[x][y-1] = 1
    
    if visited[end[0]][end[1]] == 1:
        print("#" + str(t) + " 1")
    else:
        print("#" + str(t) + " 0")