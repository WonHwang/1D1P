# 1D1P Day25 BOJ 1764번 듣보잡 문제 - 2020.11.29

import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

d_set = set()
b_set = set()

for i in range(N):
    d_set.add(sys.stdin.readline().rstrip())

for i in range(M):
    b_set.add(sys.stdin.readline().rstrip())

answer = d_set.intersection(b_set)

answer = sorted(answer)

print(len(answer))
for _ in answer:
    print(_)