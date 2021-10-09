# 1D1P Day339 BOJ 14500번 테트로미노 문제 - 2021.10.09

Max = 0

def maximize(Sum):
    global Max

    if Sum > Max:
        Max = Sum

N, M = map(int, input().split())

grid = []
for _ in range(N):
    grid.append(list(map(int, input().split())))


# 1. 맛살
# 1.1 가로
for i in range(N):
    for j in range(M-3):
        Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]
        maximize(Sum)

# 1.2 세로
for i in range(N-3):
    for j in range(M):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
        maximize(Sum)

# 2. 뭉치
for i in range(N-1):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i+1][j] + grid[i][j+1] + grid[i+1][j+1]
        maximize(Sum)

# 3. L자
# 3.1 L자
for i in range(N-2):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+2][j+1]
        maximize(Sum)

# 3.2 L자 시계방향 90도
for i in range(N-1):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j]
        maximize(Sum)

# 3.3 L자 시계방향 180도
for i in range(N-2):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1]
        maximize(Sum)

# 3.4 L자 시계방향 270도
for i in range(1, N):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i-1][j+2]
        maximize(Sum)

# 3.5 L자 대칭
for i in range(2, N):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i][j+1] + grid[i-1][j+1] + grid[i-2][j+1]
        maximize(Sum)

# 3.6 L자 대칭 시계방향 90도
for i in range(N-1):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2]
        maximize(Sum)

# 3.7 L자 대칭 시계방향 180도
for i in range(N-2):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i][j+1] + grid[i+1][j] + grid[i+2][j]
        maximize(Sum)

# 3.8 L자 대칭 시계방향 270도
for i in range(N-1):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+2]
        maximize(Sum)

# 4. 번개
# 4.1 번개
for i in range(N-2):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+1][j+1] + grid[i+2][j+1]
        maximize(Sum)

# 4.2 번개 90도
for i in range(1, N):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i-1][j+1] + grid[i-1][j+2]
        maximize(Sum)

# 4.3 번개 대칭
for i in range(N-2):
    for j in range(1, M):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+1][j-1] + grid[i+2][j-1]
        maximize(Sum)

# 4.4 번개 대칭 90도
for i in range(N-1):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i+1][j+1] + grid[i+1][j+2]
        maximize(Sum)

# 5. ㅗ
# 5.1 ㅗ
for i in range(N-1):
    for j in range(1, M-1):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+1][j-1] + grid[i+1][j+1]
        maximize(Sum)

# 5.2 ㅗ 90도
for i in range(N-2):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+1][j+1]
        maximize(Sum)

# 5.3 ㅗ 180도
for i in range(N-1):
    for j in range(M-2):
        Sum = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i+1][j+1]
        maximize(Sum)

# 5.4 ㅗ 270도
for i in range(1, N-1):
    for j in range(M-1):
        Sum = grid[i][j] + grid[i][j+1] + grid[i-1][j+1] + grid[i+1][j+1]
        maximize(Sum)

print(Max)