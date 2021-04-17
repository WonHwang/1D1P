# 1D1P Day164 BOJ 2210번 숫자판 점프 문제 - 2021.04.17

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

answer = set()

def dfs(x, y, depth, element):

    global answer

    if depth == 6:
        answer.add(element)
        return

    for i in range(4):
        a, b = x + dx[i], y + dy[i]

        if 0 <= a < 5 and 0 <= b < 5:
            dfs(a, b, depth+1, element+grid[a][b])    

grid = []

for _ in range(5):
    grid.append(list(input().split()))

for i in range(5):
    for j in range(5):
        dfs(i, j, 0, '')

print(len(answer))