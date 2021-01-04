# 1D1P Day61 BOJ 10830번 행렬 제곱 문제 - 2021.01.04

def multiple(A, B, N):

    result = [[0 for _ in range(N)] for __ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += (A[i][k] * B[k][j]) % 1000
            result[i][j] = result[i][j] % 1000
    
    return result

N, B = map(int, input().split(' '))

A = []
for _ in range(N):
    A.append(list(map(int, input().split(' '))))

B = bin(B)[2:][::-1]

answer = [[0 for _ in range(N)] for __ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            answer[i][j] = 1

i = 0
tmp = A
while i < len(B):
    if B[i] == '1':
        answer = multiple(answer, tmp, N)
    
    tmp = multiple(tmp, tmp, N)
    i += 1

for i in range(N):
    line = ""
    for _ in answer[i]:
        line += str(_) + " "
    print(line[:-1])