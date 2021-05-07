# 1D1P Day184 BOJ 2738번 행렬 덧셈 문제 - 2021.05.07

N, M = map(int, input().split())

A, B = [], []

answer = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(N):
    A.append(list(map(int, input().split())))

for _ in range(N):
    B.append(list(map(int, input().split())))

for i in range(N):
    for j in range(M):
        answer[i][j] = A[i][j] + B[i][j]

for i in range(N):
    print(*answer[i])