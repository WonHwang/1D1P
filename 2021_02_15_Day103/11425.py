# 1D1P Day103 BOJ 11425번 문자열 집합 문제 - 2021.02.15

from sys import stdin

N, M = map(int, stdin.readline().rstrip().split())

strings = {}

for i in range(N):
    strings[stdin.readline().rstrip()] = 0

answer = 0
for i in range(M):
    tmp = stdin.readline().rstrip()
    if tmp in strings:
        answer += 1

print(answer)