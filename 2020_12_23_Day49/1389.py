# 1D1P Day49 BOJ 1389번 케빈 베이컨의 6단계 법칙 - 2020.12.23

from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().rstrip().split(' '))

KB = [0] * (N+1)

relations = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, stdin.readline().rstrip().split(' '))
    relations[a].append(b)
    relations[b].append(a)

def bfs(member):
    queue = deque()
    visited = [0] * (N+1)
    queue.append([member, 0])
    visited[member] = 1

    while queue:
        node = queue.popleft()
        man, step = node[0], node[1]
        KB[member] += step
        for v in relations[man]:
            if visited[v] == 0:
                queue.append([v, step + 1])
                visited[v] = 1

for member in range(1, N+1):
    bfs(member)

answer = 1
for i in range(2, N+1):
    if KB[i] < KB[answer]:
        answer = i

print(answer)