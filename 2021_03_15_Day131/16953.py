# 1D1P Da131 BOJ 16953번 A→B 문제 - 2021.03.15

A, B = map(int, input().split())

answer = -2

def do(A, depth):
    global answer

    if A > B:
        return

    if A == B:
        answer = depth
        return

    do(2*A, depth+1)
    do(10*A + 1, depth+1)

do(A, 0)
print(answer + 1)