# 1D1P Day42 BOJ 2644번 촌수 계산 문제 - 2020.12.16

from sys import stdin
from collections import deque

N = int(stdin.readline().rstrip())
f, t = map(int, stdin.readline().rstrip().split(' '))
T = int(stdin.readline().rstrip())

relations = [[] for _ in range(N+1)]

for _ in range(T):
    a, b = map(int, stdin.readline().rstrip().split(' '))
    relations[a].append(b)
    relations[b].append(a)

visited = [0] * (N+1)

queue = deque()
queue.append([f, 0])
visited[f] = 1
answer = -1
while queue:
    node = queue.popleft()
    person = node[0]
    degree = node[1]

    if person == t:
        answer = degree
        break

    for v in relations[person]:
        if visited[v] == 0:
            queue.append([v, degree+1])
            visited[v] = 1

print(answer)