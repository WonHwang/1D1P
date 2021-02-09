# 1D1P Day97 BOJ 1652번 누울 자리를 찾아라 문제 - 2021.02.09

from sys import stdin

N = int(stdin.readline())

room = []
for _ in range(N):
    room.append(stdin.readline().rstrip())

wide_visited = [[0 for _ in range(N)] for __ in range(N)]

def wide(x, y):
    if y == N:
        return 0
    
    if room[x][y] == 'X':
        wide_visited[x][y] = 1
        return 0
    
    elif room[x][y] == '.':
        wide_visited[x][y] = 1
        return 1 + wide(x, y+1)

wide_answer = 0

for i in range(N):
    for j in range(N):
        if room[i][j] == '.' and wide_visited[i][j] == 0:
            if wide(i, j) >= 2:
                wide_answer += 1

height_visited = [[0 for _ in range(N)] for __ in range(N)]

def height(x, y):
    if x == N:
        return 0
    
    if room[x][y] == 'X':
        height_visited[x][y] = 1
        return 0
    
    elif room[x][y] == '.':
        height_visited[x][y] = 1
        return 1 + height(x+1, y)

height_answer = 0

for i in range(N):
    for j in range(N):
        if room[j][i] == '.' and height_visited[j][i] == 0:
            if height(j, i) >= 2:
                height_answer += 1

print(wide_answer, height_answer)