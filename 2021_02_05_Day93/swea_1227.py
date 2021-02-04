# 1D1P Day93 SWEA 1227번 미로 2 문제 - 2021.02.05

from collections import deque

for t in range(1, 11):
    _ = int(input())

    maze = []
    for i in range(100):
        maze.append(input())
    
    def findstart(maze):
        for i in range(100):
            for j in range(100):
                if maze[i][j] == '2':
                    return [i, j]
    
    visited = [[0 for __ in range(100)] for ___ in range(100)]
    start = findstart(maze)
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = 1
    answer = 0

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        if maze[x][y] == '3':
            answer = 1
            break

        if x > 0 and maze[x-1][y] != '1' and visited[x-1][y] == 0:
            queue.append([x-1, y])
            visited[x-1][y] = 1
        
        if y > 0 and maze[x][y-1] != '1' and visited[x][y-1] == 0:
            queue.append([x, y-1])
            visited[x][y-1] = 1
        
        if x < 99 and maze[x+1][y] != '1' and visited[x+1][y] == 0:
            queue.append([x+1, y])
            visited[x+1][y] = 1

        if y < 99 and maze[x][y+1] != '1' and visited[x][y+1] == 0:
            queue.append([x, y+1])
            visited[x][y+1] = 1

    print(f"#{t} {answer}")