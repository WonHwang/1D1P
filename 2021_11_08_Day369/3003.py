# 1D1P Day369 BOJ 3003번 킹, 퀸, 룩, 비숍, 나이트, 폰 문제 - 2021.11.08

answer = [1, 1, 2, 2, 2, 8]
now = list(map(int, input().split()))
for i in range(6):
    answer[i] -= now[i]

print(*answer)