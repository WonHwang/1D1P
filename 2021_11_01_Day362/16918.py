# 1D1P Day362 BOJ 16918번 봄버맨 문제 - 2021.11.01

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

R, C, N = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(list(input()))

status = [[0 for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            status[i][j] = 3

cnt = 0
while cnt < N:
    cnt += 1
    bomb = []
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 'O':
                if status[i][j] == 1:
                    bomb.append([i, j])
                status[i][j] -= 1
    
    while bomb:
        node = bomb.pop()
        grid[node[0]][node[1]] = '.'
        for i in range(4):
            x, y = node[0] + dx[i], node[1] + dy[i]
            if 0 <= x < R and 0 <= y < C:
                grid[x][y] = '.'
                status[x][y] = 0
    
    if not cnt%2:
        for i in range(R):
            for j in range(C):
                if grid[i][j] == '.':
                    grid[i][j] = 'O'
                    status[i][j] = 3

for i in range(R):
    print(''.join(grid[i]))