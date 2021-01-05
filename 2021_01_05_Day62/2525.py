# 1D1P Day62 BOJ 2525번 오븐 시계 문제 - 2021.01.05

A, B = map(int, input().split(' '))
C = int(input())

M = B + C
H = (A + ((B + C) // 60)) % 24
M = M % 60

print(H, M)