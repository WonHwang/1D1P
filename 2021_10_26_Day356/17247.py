# 1D1P Day356 BOJ 17247번 택시 거리 문제 - 2021.10.26

N, M = map(int, input().split())
grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))

target = []

for i in range(N):
    for j in range(M):
        if grid[i][j] == 1:
            target.append([i, j])
    if len(target) == 2:
        break

print(abs(target[0][0] - target[1][0]) + abs(target[0][1] - target[1][1]))