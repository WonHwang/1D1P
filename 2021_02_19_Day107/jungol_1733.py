# 1D1P Day107 JUNGOL 1733번 오목 문제 - 2021.02.19

board = []

def isfive(x, y, color):

    answer = 0
    if x <= 14:
        answer = 1
        for i in range(1, 5):
            if board[x+i][y] != color:
                answer = 0
                break

        if answer:
            if x < 14 and board[x+5][y] == color:
                answer = 0
            if x > 0 and board[x-1][y] == color:
                answer = 0

            if answer:
                return answer
    
    if y <= 14:
        answer = 1
        for i in range(1, 5):
            if board[x][y+i] != color:
                answer = 0
                break
    
        if answer:
            if y < 14 and board[x][y+5] == color:
                answer = 0
            if y > 0 and board[x][y-1] == color:
                answer = 0
            if answer:
                return answer

    if x <= 14 and y <= 14:
        answer = 1
        for i in range(1, 5):
            if board[x+i][y+i] != color:
                answer = 0
                break
    
        if answer:
            if x < 14 and y < 14 and board[x+5][y+5] == color:
                answer = 0
            if x > 0 and y > 0 and board[x-1][y-1] == color:
                answer = 0
            
            if answer:
                return answer
    
    if x >= 4 and y <= 14:
        answer = 1
        for i in range(1, 5):
            if board[x-i][y+i] != color:
                answer = 0
                break
        
        if answer:
            if y < 14 and x > 4 and board[x-5][y+5] == color:
                answer = 0
            if y > 0 and x < 18 and board[x+1][y-1] == color:
                answer = 0
            if answer:
                return answer
    
    return answer


for _ in range(19):
    board.append(list(map(int, input().split())))


answer = 0
target = [0, 0]
for i in range(19):
    for j in range(19):

        if board[i][j] == 1:
            if isfive(i, j, 1):
                answer = 1
                target = [i, j]
                break
        
        elif board[i][j] == 2:
            if isfive(i, j, 2):
                answer = 2
                target = [i, j]
                break
    
    if answer:
        break

if answer:
    print(answer)
    print(target[0]+1, target[1]+1)

else:
    print(answer)