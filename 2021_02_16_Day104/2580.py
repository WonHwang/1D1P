def row(x, y, sudoku):

    visited = [0] * 9
    
    numofzero = 0
    for i in range(9):
        if sudoku[x][i] == 0:
            numofzero += 1
        visited[sudoku[x][i] - 1] = 1
    
    if numofzero > 1 or numofzero == 0:
        return False
    
    tmp = -1
    for i in range(9):
        if visited[i] == 0:
            tmp = i
            break
    if tmp >= 0:
        sudoku[x][y] = tmp + 1
        return True
    return False

def column(x, y, sudoku):
    
    visited = [0] * 9

    numofzero = 0
    for i in range(9):
        if sudoku[i][y] == 0:
            numofzero += 1
        visited[sudoku[i][y] -1] = 1
    
    if numofzero > 1 or numofzero == 0:
        return False

    tmp = -1
    for i in range(9):
        if visited[i] == 0:
            tmp = i
            break
    if tmp >= 0:
        sudoku[x][y] = tmp + 1
        return True
    return False

def square(x, y, sudoku):
    
    visited = [0] * 9

    numofzero = 0

    for i in range((x // 3) * 3, ((x // 3) * 3) + 3):
        for j in range((y // 3) * 3, ((y // 3) * 3) + 3):
            if sudoku[i][j] == 0:
                numofzero += 1
            visited[sudoku[i][j] - 1] = 1
    
    if numofzero > 1 or numofzero == 0:
        return False

    tmp = -1
    for i in range(9):
        if visited[i] == 0:
            tmp = i
            break
    
    if tmp >= 0:
        sudoku[x][y] = tmp + 1
        return True
    return False
    


sudoku = []

for _ in range(9):
    sudoku.append(list(map(int, input().split())))

numofzero = 0
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            numofzero += 1

while True:
    numofzero = 0
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                numofzero += 1
                if row(i, j, sudoku):
                    print("doesnt work?")
                    continue
                if column(i, j, sudoku):
                    continue
                if square(i, j, sudoku):
                    continue
    if not numofzero:
        break


    for i in range(9):
        print(sudoku[i])
    print(numofzero)

for i in range(9):
    print(sudoku[i])