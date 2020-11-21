# 1D1P Day21 BOJ 4963번 섬의 개수 문제 - 2020.11.21

import sys
from collections import deque

while True:
    w, h = map(int, input().split(' '))
    if w == 0 and h == 0:
        break

    maps = []
    for i in range(h):
        line = sys.stdin.readline().rstrip().split(' ')
        for j in range(w):
            line[j] = int(line[j])
        maps.append(line)
    
    visited = [[0 for i in range(w)] for j in range(h)]

    def search(i, j):

        queue = deque()
        queue.append([i, j])
        while queue:
            node = queue.popleft()
            x = node[0]
            y = node[1]
            if visited[x][y] == 0:
                visited[x][y] = 1
                if x > 0:
                    if maps[x-1][y] == 1 and visited[x-1][y] == 0:
                        queue.append([x-1, y])
                if x < h-1:
                    if maps[x+1][y] == 1 and visited[x+1][y] == 0:
                        queue.append([x+1, y])
                if y > 0:
                    if maps[x][y-1] == 1 and visited[x][y-1] == 0:
                        queue.append([x, y-1])
                if y < w-1:
                    if maps[x][y+1] == 1 and visited[x][y+1] == 0:
                        queue.append([x,y+1])
                if x > 0 and y > 0:
                    if maps[x-1][y-1] == 1 and visited[x-1][y-1] == 0:
                        queue.append([x-1, y-1])
                if x > 0 and y < w-1:
                    if maps[x-1][y+1] == 1 and visited[x-1][y+1] == 0:
                        queue.append([x-1, y+1])
                if x < h-1 and y > 0:
                    if maps[x+1][y-1] == 1 and visited[x+1][y-1] == 0:
                        queue.append([x+1, y-1])
                if x < h-1 and y < w-1:
                    if maps[x+1][y+1] == 1 and visited[x+1][y+1] == 0:
                        queue.append([x+1, y+1])
    
    answer = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1 and visited[i][j] == 0:
                search(i, j)
                answer += 1
    
    print(answer)