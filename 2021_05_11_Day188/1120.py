# 1D1P Day188 BOJ 1120번 문자열 문제 - 2021.05.11

A, B = map(str, input().split())


gap = len(B)

for i in range(len(B) - len(A) + 1):
    tmp = 0
    for a in range(len(A)):
        if B[i+a] != A[a]:
            tmp += 1
    
    if tmp < gap:
        gap = tmp

print(gap)