# 1D1P Day276 BOJ 1247번 부호 문제 - 2021.08.07

from sys import stdin
input = stdin.readline

for _ in range(3):
    N = int(input())
    total = 0
    for _ in range(N):
        total += int(input())
    if total > 0:
        print('+')
    elif total < 0:
        print('-')
    else:
        print(0)