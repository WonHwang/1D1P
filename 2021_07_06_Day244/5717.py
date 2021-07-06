# 1D1P Day244 BOJ 5717번 상근이의 친구들 문제 - 2021.07.06

from sys import stdin
input = stdin.readline

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)