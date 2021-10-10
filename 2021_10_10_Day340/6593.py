# 1D1P Day340 BOJ 6593번 상범 빌딩 문제 - 2021.10.10

from collections import deque

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    L, R, C = map(int, input().split())

    if not L and not R and not C:
        break

    grid = []
    for _ in range(L):
        tmp = []
        for __ in range(R):
            tmp.append(list(input()))
        garbage = input()
        grid.append(tmp)

    start = []
    end = []
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if grid[i][j][k] == 'S':
                    start = [i, j, k]
                if grid[i][j][k] == 'E':
                    end = [i, j, k]
            if start and end:
                break
        if start and end:
            break

    queue = deque()
    visited = [[[0 for _ in range(C)] for __ in range(R)] for ___ in range(L)]
    visited[start[0]][start[1]][start[2]] = 1
    queue.append(start)

    while queue:
        node = queue.popleft()
        x, y, z = node[0], node[1], node[2]
        step = visited[x][y][z]

        if grid[x][y][z] == 'E':
            break

        for i in range(6):
            x_, y_, z_ = x + dx[i], y + dy[i], z + dz[i]

            if 0 <= x_ < L and 0 <= y_ < R and 0 <= z_ < C and not visited[x_][y_][z_] and grid[x_][y_][z_] != '#':
                visited[x_][y_][z_] = step + 1
                queue.append([x_, y_, z_])

    x, y, z = end[0], end[1], end[2]
    if visited[x][y][z]:
        answer = visited[x][y][z] - 1
    else:
        answer = 0

    print(f"Escaped in {answer} minute(s)." if answer else "Trapped!")