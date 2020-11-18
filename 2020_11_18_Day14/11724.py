# 1D1P Day14 BOJ 11724번 연결 요소의 개수 문제 - 2020.11.18

import sys

N, M = map(int, sys.stdin.readline().rstrip().split(' '))

graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for i in range(N+1)]
answer = 0

for i in range(1, N+1):
    if visited[i] == 0:
        queue = []
        queue.append(i)
        visited[i] = 1
        while queue:
            node = queue.pop(0)
            visited[node] = 1
            for j in graph[node]:
                if visited[j] == 0:
                    queue.append(j)
        answer += 1

print(answer)