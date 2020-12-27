# 1D1P Day53 BOJ 7562번 나이트의 이동 문제 - 2020.12.27

from sys import stdin
from collections import deque

def bfs(N, From, To):
    visited = [[0 for _ in range(N)] for __ in range(N)]
    queue = deque()
    queue.append(From)
    visited[From[0]][From[1]] = 1
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        step = visited[x][y]
        if x == To[0] and y == To[1]:
            break
        
        if x-1 >= 0 and y+2 <= N-1:
            if visited[x-1][y+2] == 0:
                queue.append([x-1, y+2])
                visited[x-1][y+2] = step+1
        if x-2 >= 0 and y+1 <= N-1:
            if visited[x-2][y+1] == 0:
                queue.append([x-2, y+1])
                visited[x-2][y+1] = step+1
        if x-2 >= 0 and y-1 >= 0:
            if visited[x-2][y-1] == 0:
                queue.append([x-2, y-1])
                visited[x-2][y-1] = step+1
        if x-1 >= 0 and y-2 >= 0:
            if visited[x-1][y-2] == 0:
                queue.append([x-1, y-2])
                visited[x-1][y-2] = step+1
        if x+1 <= N-1 and y-2 >= 0:
            if visited[x+1][y-2] == 0:
                queue.append([x+1, y-2])
                visited[x+1][y-2] = step+1
        if x+2 <= N-1 and y-1 >= 0:
            if visited[x+2][y-1] == 0:
                queue.append([x+2, y-1])
                visited[x+2][y-1] = step+1
        if x+1 <= N-1 and y+2 <= N-1:
            if visited[x+1][y+2] == 0:
                queue.append([x+1, y+2])
                visited[x+1][y+2] = step+1
        if x+2 <= N-1 and y+1 <= N-1:
            if visited[x+2][y+1] == 0:
                queue.append([x+2, y+1])
                visited[x+2][y+1] = step+1
    
    return step


T = int(stdin.readline().rstrip())

for _ in range(T):
    N = int(stdin.readline().rstrip())
    from_x, from_y = map(int, stdin.readline().rstrip().split(' '))
    to_x, to_y = map(int, stdin.readline().rstrip().split(' '))
    step = bfs(N, [from_x, from_y], [to_x, to_y])
    print(step - 1)