# 1D1P Day90 SWEA 11315번 오목 문제 - 2021.02.02

for t in range(1, int(input()) + 1):
    N = int(input())
    board = []
    for i in range(N):
        board.append(input())
    
    answer = 0
    for i in range(N):
        for j in range(N-4):
            if board[i][j] == 'o' and board[i][j+1] == 'o' and board[i][j+2] == 'o' and board[i][j+3] == 'o' and board[i][j+4] == 'o':
                answer = 1
                break
    
    if not answer:
        for i in range(N):
            for j in range(N-4):
                if board[j][i] == 'o' and board[j+1][i] == 'o' and board[j+2][i] == 'o' and board[j+3][i] == 'o' and board[j+4][i] == 'o':
                    answer = 1
                    break
    
    if not answer:
        for i in range(N-4):
            for j in range(N-4):
                if board[i][j] == 'o' and board[i+1][j+1] == 'o' and board[i+2][j+2] == 'o' and board[i+3][j+3] == 'o' and board[i+4][j+4] == 'o':
                    answer = 1
                    break
    
    if not answer:
        for i in range(N-4):
            for j in range(N-1, 3, -1):
                if board[i][j] == 'o' and board[i+1][j-1] == 'o' and board[i+2][j-2] == 'o' and board[i+3][j-3] == 'o' and board[i+4][j-4] == 'o':
                    answer = 1
                    break
    
    if answer:
        print(f"#{t} YES")
    else:
        print(f"#{t} NO")