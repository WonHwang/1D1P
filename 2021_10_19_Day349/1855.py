# 1D1P Day349 BOJ 1855번 암호 문제 - 2021.10.19

K = int(input())
E = input()
P = ""
N = len(E) // K

table = [['' for _ in range(K)] for _ in range(N)]

idx = 0
for i in range(N):
    if i%2:
        for j in range(K-1, -1, -1):
            table[i][j] = E[idx]
            idx += 1
    else:
        for j in range(K):
            table[i][j] = E[idx]
            idx += 1

for i in range(K):
    for j in range(N):
        P += table[j][i]

print(P)