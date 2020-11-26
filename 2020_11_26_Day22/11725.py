# 1D1P Day22 BOJ 11725번 트리의 부모 찾기 문제 - 2020.11.26

import sys
from collections import deque
N = int(input())

information = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    information[a].append(b)
    information[b].append(a)

visited = [0] * (N+1)

queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    node = queue.popleft()
    for i in information[node]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = node

for i in range(2, N+1):
    print(visited[i])