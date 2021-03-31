# 1D1P Day147 BOJ 12026번 BOJ거리 문제 - 2021.03.31

N = int(input())
board = input()
DP = [0] * N
DP[0] = 1
for i in range(N):

    if not DP[i]:
        continue

    if board[i] == 'B':
        for j in range(i+1, N):
            if board[j] == 'O':
                if DP[j]:
                    DP[j] = min(DP[j], DP[i] + (j-i)**2)
                else:
                    DP[j] = DP[i] + (j-i)**2
    elif board[i] == 'O':
        for j in range(i+1, N):
            if board[j] == 'J':
                if DP[j]:
                    DP[j] = min(DP[j], DP[i] + (j-i)**2)
                else:
                    DP[j] = DP[i] + (j-i)**2
    elif board[i] == 'J':
        for j in range(i+1, N):
            if board[j] == 'B':
                if DP[j]:
                    DP[j] = min(DP[j], DP[i] + (j-i)**2)
                else:
                    DP[j] = DP[i] + (j-i)**2

print(DP[N-1]-1 if DP[N-1] else -1)