# 1D1P Day15 BOJ 11724번 연결 요소의 개수 문제 - 2020.11.19 - 18일에 못품..

import sys

def bfs(v):
    queue = [v]
    while queue:
        node = queue.pop(0)
        for value in graph[node]:
            if visited[value] == 0:
                queue.append(value)
                visited[value] = 1

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
answer = 0

for i in range(1, N+1):
    if visited[i] == 0:
        bfs(i)
        answer += 1

print(answer)