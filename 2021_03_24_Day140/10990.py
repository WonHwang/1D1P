# 1D1P Day140 BOJ 10990번 별 찍기 - 15 문제 - 2021.03.24

N = int(input())
for i in range(N):
    gap = N-1-i
    for j in range(2*N-1):
        if j == 2*N - 2 - gap:
            print('*')
            break
        elif j == gap:
            print('*', end='')
        else:
            print(' ', end='')