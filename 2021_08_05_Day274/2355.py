# 1D1P Day274 BOJ 2355번 시그마 문제 - 2021.08.05

def sigma(A, B):
    if A > B:
        A, B = B, A
    return (B-A+1)*(A+B)//2

A, B = map(int, input().split())
print(sigma(A, B))