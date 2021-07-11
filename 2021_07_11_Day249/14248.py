# 1D1P Day249 BOJ 14248번 점프 점프 문제 - 2021.07.11

from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
stone = list(map(int, input().split()))
start = int(input())
visited = [0] * N
queue = deque()
queue.append(start-1)
visited[start-1] = 1
answer = 0

while queue:
    node = queue.popleft()
    answer += 1

    for next in [node-stone[node], node+stone[node]]:
        if 0 <= next < N and not visited[next]:
            visited[next] = 1
            queue.append(next)

print(answer)