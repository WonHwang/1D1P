# 1D1P Day29 BOJ 1967번 트리의 지름 문제 - 2020.12.03

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())

info = [[] for _ in range(N+1)]

for _ in range(N-1):
    f, t, w = map(int, stdin.readline().rstrip().split(' '))
    info[f].append([t, w])
    info[t].append([f, w])

visited = [0] * (N+1)

queue = deque()
queue.append([1, 0])
visited[1] = 1


max_weight = 0
max_node = 0

while queue:
    node = queue.popleft()
    f, w = node[0], node[1]

    if w > max_weight:
        max_weight = w
        max_node = f

    for i in info[f]:
        if visited[i[0]] == 0:
            queue.append([i[0], i[1] + w])
            visited[i[0]] = 1

visited = [0] * (N+1)

queue = deque()
queue.append([max_node, 0])
visited[max_node] = 1


max_weight = 0
max_node = 0

while queue:
    node = queue.popleft()
    f, w = node[0], node[1]

    if w > max_weight:
        max_weight = w
        max_node = f

    for i in info[f]:
        if visited[i[0]] == 0:
            queue.append([i[0], i[1] + w])
            visited[i[0]] = 1

print(max_weight)