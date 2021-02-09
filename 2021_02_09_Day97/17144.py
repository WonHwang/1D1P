# 1D1P Day97 BOJ 17144번 미세먼지 안녕! 문제 - 2021.02.09

from sys import stdin
from collections import deque

R, C, T = map(int, stdin.readline().rstrip().split())

room = []

for _ in range(R):
    room.append(list(map(int, stdin.readline().rstrip().split())))

right = []

for i in range(R):
    if room[i][0] == -1:
        right.append(i)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def next_index(x, y):
    if (x == (right[0] - 1) and y == 0) or (x == (right[1] + 1) and y == 0):
        return -1, -1
    
    elif x == 0 and y == 0:
        return x+1, y
    
    elif x == 0 and y == C-1:
        return x, y-1
    
    elif x == R-1 and y == 0:
        return x-1, y
    
    elif x == R-1 and y == C-1:
        return x, y-1
    
    elif x == right[0] and y == C-1:
        return x-1, y
    
    elif x == right[1] and y == C-1:
        return x+1, y
    
    elif x in right and y != C-1 and y != 0:
        return x, y+1
    
    elif x == 0 and y != 0 and y != C-1:
        return x, y-1
    
    elif x == R-1 and y != 0 and y != C-1:
        return x, y-1
    
    elif y == C-1 and  x <= right[0] - 1 and x != 0:
        return x-1, y
    
    elif y == C-1 and x >= right[1] + 1 and x != R-1:
        return x+1, y
    
    elif y == 0 and x < right[0] - 1 and x != 0:
        return x+1, y
    
    elif y == 0 and x > right[1] + 1 and x != R-1:
        return x-1, y
    
    else:
        return x, y

def spread(room):

    temp = [[0 for _ in range(C)] for __ in range(R)]

    for i in range(R):
        for j in range(C):
            if room[i][j] > 4:
                amount = room[i][j] // 5

                number = 0

                for k in range(4):
                    if i+dx[k] >= 0 and i+dx[k] < R and j+dy[k] >= 0 and j+dy[k] < C and room[i+dx[k]][j+dy[k]] != -1:
                        temp[i+dx[k]][j+dy[k]] += amount
                        number += 1
                
                temp[i][j] += (room[i][j] - amount * number)
            
            elif room[i][j] > 0 and room[i][j] <= 4:
                temp[i][j] += room[i][j]
            
            elif room[i][j] == -1:
                temp[i][j] = -1
    return temp

def rotation(room):
    temp = [[0 for _ in range(C)] for __ in range(R)]
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                x, y = next_index(i, j)

                if x == -1 and y == -1:
                    continue
                temp[x][y] = room[i][j]

            elif room[i][j] == -1:
                temp[i][j] = room[i][j]
    return temp

for _ in range(T):
    room = spread(room)
    room = rotation(room)

answer = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            answer += room[i][j]

print(answer)