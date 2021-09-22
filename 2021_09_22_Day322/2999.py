# 1D1P Day322 BOJ 2999번 비밀 이메일 문제 - 2021.09.22

P = input()
N = len(P)

for i in range(1, int(N**0.5)+1):
    if not N%i:
        R = i

C = N // R

arr = [['' for _ in range(C)] for _ in range(R)]

for i in range(C):
    for j in range(R):
        arr[j][i] = P[i*R + j]

answer = ''
for i in range(R):
    for j in range(C):
        answer += arr[i][j]

print(answer)