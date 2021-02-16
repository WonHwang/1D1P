# 1D1P Day104 BOJ 17135번 캐슬디펜스 문제 - 2021.02.16

from collections import deque
import copy

N, M, D = map(int, input().split())

castle = []

for _ in range(N):
    castle.append(list(map(int, input().split())))
castle.append([0 for _ in range(M)])

saved_castle = copy.deepcopy(castle)

answer = 0

def findenemy(i, a):
    visited = [[-1 for _ in range(M)] for _ in range(N+1)]
    queue = deque()
    queue.append([i, a])
    visited[i][a] = 0

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        step = visited[x][y]

        if castle[x][y] == 1 and step <= D:
            return [x, y]

        if y > 0:
            if visited[x][y-1] == -1:
                queue.append([x, y-1])
                visited[x][y-1] = step + 1
        
        if x > 0:
            if visited[x-1][y] == -1:
                queue.append([x-1, y])
                visited[x-1][y] = step + 1
        
        if y < M-1:
            if visited[x][y+1] == -1:
                queue.append([x, y+1])
                visited[x][y+1] = step + 1

def isthereenemy():
    for i in range(N):
        for j in range(M):
            if castle[i][j] == 1:
                return True
    return False

def kill(i, a, b, c):

    global answer

    target = []
    target.append(findenemy(i, a))
    target.append(findenemy(i, b))
    target.append(findenemy(i, c))

    for grid in target:
        if grid:
            x, y = grid[0], grid[1]
            if castle[x][y] == 1:
                castle[x][y] = 0
                answer += 1

def movedown():
    
    for i in range(N-2, -1, -1):
        for j in range(M):
            castle[i+1][j] = castle[i][j]
    
    for i in range(1):
        for j in range(M):
            castle[i][j] = 0

Max = 0

for a in range(M-2):
    for b in range(a+1, M-1):
        for c in range(b+1, M):
            answer = 0
            castle = copy.deepcopy(saved_castle)

            for j in range(N):
                if isthereenemy:
                    kill(N, a, b, c)
                    movedown()
                
            if answer > Max:
                Max = answer

print(Max)