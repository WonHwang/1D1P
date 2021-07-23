# 1D1P Day261 BOJ 2578번 빙고 문제 - 2021.07.23

from sys import stdin
input = stdin.readline

def check(board):
    answer = 0
    for i in range(5):
        for j in range(5):
            if board[i][j]:
                break
        else:
            answer += 1
    
    for i in range(5):
        for j in range(5):
            if board[j][i]:
                break
        else:
            answer += 1
    
    for i in range(5):
        if board[i][i]:
            break
    else:
        answer += 1
    
    for i in range(5):
        if board[i][4-i]:
            break
    else:
        answer += 1
    
    return answer

board = []
for _ in range(5):
    board.append(list(map(int, input().split())))

target = []
for _ in range(5):
    target.extend(list(map(int, input().split())))

for i in range(25):
    
    flag = 0
    for a in range(5):
        for b in range(5):
            if board[a][b] == target[i]:
                board[a][b] = 0
                flag = 1
                break
        if flag:
            break
    
    if check(board) >= 3:
        print(i+1)
        break