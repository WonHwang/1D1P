def iscorrect(sudoku):
    onetonine = [i for i in range(1, 10)]

    for i in range(9):
        if sorted(sudoku[i]) != onetonine:
            return False
    
    for i in range(9):
        tmp = []
        for j in range(9):
            tmp.append(sudoku[j][i])
        if sorted(tmp) != onetonine:
            return False

    for i in range(3):
        for j in range(3):
            tmp = []
            for x in range(3*i, 3*i+3):
                for y in range(3*j, 3*j+3):
                    tmp.append(sudoku[x][y])
            if sorted(tmp) != onetonine:
                return False
    return True
T = int(input())

for _ in range(T):
    sudoku = []
    for __ in range(9):
        sudoku.append(list(map(int, input().split(' '))))
    
    print(f"#{_+1} {int(iscorrect(sudoku))}")