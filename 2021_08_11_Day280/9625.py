# 1D1P Day280 BOJ 9625번 BABBA 문제 - 2021.08.11

N = int(input())
A, B = 1, 0

for _ in range(N):
    A, B = B, A + B

print(A, B)