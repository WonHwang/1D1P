# 1D1P Day28 BOJ 1167번 트리의 지름 문제 - 2020.12.02

from sys import stdin
from collections import deque

V = int(stdin.readline().rstrip())

info = [[] for _ in range(V+1)]

for i in range(V):
    input_ = stdin.readline().rstrip().split(' ')
    length = len(input_)
    for i in range(length):
        input_[i] = int(input_[i])
    for i in range(int(length/2)-1):
        info[input_[0]].append([input_[2*i + 1], input_[2*i + 2]])

visited = [0] * (V+1)

queue = deque()
queue.append([1, 0])
visited[1] = 1
maximum = 0
v1 = 0

while queue:
    node = queue.popleft()
    v = node[0]
    dis = node[1]
    if maximum < dis:
        maximum = dis
        v1 = v
    for i in info[v]:
        if visited[i[0]] == 0:
            queue.append([i[0], i[1]+dis])
            visited[i[0]] = 1

queue = deque()
queue.append([v1, 0])
visited = [0] * (V+1)
visited[v1] = 1
miximum = 0
v2 = 0

while queue:
    node = queue.popleft()
    v = node[0]
    dis = node[1]
    if maximum < dis:
        maximum = dis
        v2 = v
    for i in info[v]:
        if visited[i[0]] == 0:
            queue.append([i[0], i[1]+dis])
            visited[i[0]] = 1

print(maximum)