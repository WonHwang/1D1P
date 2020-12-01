# 1D1P Day27 BOJ 2606번 바이러스 문제 - 2020.12.01

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
M = int(stdin.readline().rstrip())

network = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split(' '))
    network[a].append(b)
    network[b].append(a)

queue = deque()
queue.append(1)
visited[1] = 1

while queue:
    node = queue.popleft()
    for v in network[node]:
        if visited[v] == 0:
            queue.append(v)
            visited[v] = 1

answer = 0
for i in range(2, N+1):
    if visited[i] == 1:
        answer += 1

print(answer)