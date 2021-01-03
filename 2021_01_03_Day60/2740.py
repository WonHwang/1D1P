N, M = map(int, input().split(' '))
A = []
for _ in range(N):
    A.append(list(map(int, input().split(' '))))

M, K = map(int, input().split(' '))

B = []
for _ in range(M):
    B.append(list(map(int, input().split(' '))))

result = [[0 for _ in range(K)] for __ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

for i in range(N):
    answer = ""
    for j in range(K):
        answer += str(result[i][j]) + " "
    print(answer[:-1])