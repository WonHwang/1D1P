# 1D1P Day115 BOJ 2580번 스도쿠 문제 - 2021.02.27

sudoku = []

for _ in range(9):
    sudoku.append(list(map(int, input().split())))

zeros = []

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append((i, j))

def promising(x, y):

    target = [i for i in range(1, 10)]

    for i in range(9):
        if sudoku[x][i] in target:
            target.remove(sudoku[x][i])
        if sudoku[i][y] in target:
            target.remove(sudoku[i][y])
    
    for i in range(3 * (x // 3), 3 * (x // 3) + 3):
        for j in range(3 * (y // 3), 3 * (y // 3) + 3):
            if sudoku[i][j] in target:
                target.remove(sudoku[i][j])
    
    return target

flag = False
def dfs(x):
    global flag

    if flag:
        return

    if x == len(zeros):
        for i in range(9):
            print(*sudoku[i])
            flag = True
        return
    
    else:
        (a, b) = zeros[x]
        target = promising(a, b)
        for number in target:
            sudoku[a][b] = number
            dfs(x+1)
            sudoku[a][b] = 0

dfs(0)