# 1D1P Day137 BOJ 11559번 Puyo Puyo 문제 - 2021.03.21

from sys import stdin
from collections import deque

input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def drop(field):
    for i in range(6): 
        field[i] = list(''.join(''.join(field[i]).split('0'))[::-1].zfill(12)[::-1])

def bfs(x, y, color, visited, field):

    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    count = 0

    while queue:
        node = queue.popleft()
        count += 1
        a, b = node[0], node[1]

        for i in range(4):
            x_, y_ = a + dx[i], b + dy[i]

            if 0 <= x_ <= 5 and 0 <= y_ <= 11 and field[x_][y_] == color and visited[x_][y_] == 0:
                visited[x_][y_] = 1
                queue.append([x_, y_])

    return count

def bfsforchangecolor(x, y, color, field):

    queue = deque()
    visited = [[0 for _ in range(12)] for _ in range(6)]
    queue.append([x, y])
    visited[x][y] = 1

    while queue:
        node = queue.popleft()
        a, b = node[0], node[1]
        field[a][b] = '0'

        for i in range(4):
            x_, y_ = a + dx[i], b + dy[i]
            if 0 <= x_ <= 5 and 0 <= y_ <= 11 and visited[x_][y_] == 0 and field[x_][y_] == color:
                visited[x_][y_] = 1
                queue.append([x_, y_])

field = []

tmp = []
for i in range(12):
    tmp.append(input())

for i in range(6):
    string = ""
    for j in range(12):
        if tmp[11-j][i] == '.':
            string += '0'
        else:
            string += tmp[11-j][i]
    
    field.append(list(string))

did = False
answer = 0
while True:

    visited = [[0 for _ in range(12)] for _ in range(6)]

    for i in range(6):
        for j in range(12):
            if field[i][j] != '0' and visited[i][j] == 0:
                count = bfs(i, j, field[i][j], visited, field)

                if count >= 4:
                    did = True
                    bfsforchangecolor(i, j, field[i][j], field)
    
    if did:
        answer += 1
        drop(field)

    else:
        break

    did = False

print(answer)