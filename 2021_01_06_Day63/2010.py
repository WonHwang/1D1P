# 1D1P Day63 BOJ 2010번 플러그 문제 - 2021.01.06

from sys import stdin

N = int(stdin.readline().rstrip())

result = 1
for _ in range(N):
    result += int(stdin.readline().rstrip()) -1

print(result)