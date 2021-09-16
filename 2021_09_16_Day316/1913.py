# 1D1P Day316 BOJ 1913번 달팽이 문제 - 2021.09.16

N = int(input())

grid = [[0 for _ in range(N)] for _ in range(N)]

x = y = N // 2
if not N % 2:
    y -= 1

direction = 0
step = [1, 0, 0]

for i in range(1, N**2 + 1):
    grid[x][y] = i

    if i == N**2:
        break

    if direction == 0:
        x -= 1
    
    elif direction == 1:
        y += 1
    
    elif direction == 2:
        x += 1
    
    elif direction == 3:
        y -= 1
    
    step[1] += 1

    if step[0] == step[1]:
        step[2] += 1
        step[1] = 0
        direction  = (direction + 1) % 4
    
    if step[2] == 2:
        step[2] = 0
        step[0] += 1

for i in range(N):
    print(*grid[i])

target = int(input())

answer = []
for i in range(N):
    for j in range(N):
        if grid[i][j] == target:
            answer = [i+1, j+1]
            break
    if answer:
        break

print(*answer)