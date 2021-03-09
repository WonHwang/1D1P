# 1D1P Day125 BOJ 2217번 로프 문제 - 2021.03.09

from sys import stdin
input = stdin.readline

N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
answer = rope[0]
cnt = 1
for i in range(1, N):
    cnt += 1
    tmp = cnt * rope[i]
    if tmp > answer:
        answer = tmp
print(answer)