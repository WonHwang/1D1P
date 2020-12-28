# 1D1P Day54 BOJ 2636번 치즈 문제 - 2020.12.28

from sys import stdin
from collections import deque

H, W = map(int, stdin.readline().rstrip().split(' '))

cheese = []

for _ in range(H):
    cheese.append(stdin.readline().rstrip().split(' '))

def findcrust(queue_crust):
    visited = [[0 for _ in range(W)] for __ in range(H)]
    queue = deque()
    queue.append([0,0])
    visited[0][0] = 1

    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]

        if x > 0:
            if cheese[x-1][y] == '0' and visited[x-1][y] == 0:
                queue.append([x-1, y])
                visited[x-1][y] = 1
            if cheese[x-1][y] == '1' and visited[x-1][y] == 0:
                queue_crust.append([x-1, y])
                visited[x-1][y] = 1
        if y > 0:
            if cheese[x][y-1] == '0' and visited[x][y-1] == 0:
                queue.append([x, y-1])
                visited[x][y-1] = 1
            if cheese[x][y-1] == '1' and visited[x][y-1] == 0:
                queue_crust.append([x, y-1])
                visited[x][y-1] = 1
        if x < H-1:
            if cheese[x+1][y] == '0' and visited[x+1][y] == 0:
                queue.append([x+1, y])
                visited[x+1][y] = 1
            if cheese[x+1][y] == '1' and visited[x+1][y] == 0:
                queue_crust.append([x+1, y])
                visited[x+1][y] = 1
        if y < W-1:
            if cheese[x][y+1] == '0' and visited[x][y+1] == 0:
                queue.append([x, y+1])
                visited[x][y+1] = 1
            if cheese[x][y+1] == '1' and visited[x][y+1] == 0:
                queue_crust.append([x, y+1])
                visited[x][y+1] = 1
    return queue_crust

queue = deque()
queue = findcrust(queue)
time = 0
last_crust = 0
while len(queue) > 0:
    time += 1
    last_crust = len(queue)
    while queue:
        node = queue.popleft()
        x, y = node[0], node[1]
        cheese[x][y] = '0'
    queue = findcrust(queue)

print(time)
print(last_crust)