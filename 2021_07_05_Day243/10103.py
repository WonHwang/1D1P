# 1D1P Day243 BOJ 10103번 주사위 게임 문제 - 2021.07.05
from sys import stdin
input = stdin.readline
A, B = 100, 100
for _ in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        B -= a
    elif b > a:
        A -= b

print(A)
print(B)