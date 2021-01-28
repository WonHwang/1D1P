# 1D1P Day67 BOJ 1753번 최단경로 문제 - 2021.01.10
# 다익스트라 기본문제
# 우선순위 큐의 사용이 필수적.

import sys
import heapq

V, E = map(int, sys.stdin.readline().rstrip().split(' '))
start = int(sys.stdin.readline().rstrip())
adj = [{} for _ in range(V+1)]
INF = 3000000

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().rstrip().split(' '))
    if v not in adj[u]:
        adj[u][v] = w
    else:
        if adj[u][v] > w:
            adj[u][v] = w

for i in range(1, V+1):
    adj[i][i] = 0

distance = [INF] * (V+1)
distance[start] = 0
queue = []
heapq.heappush(queue, (0, start)) # iterable 첫번째 원소를 기준으로 heapify

while queue:
    node = heapq.heappop(queue)
    for v in adj[node[1]]:
        if distance[v] > node[0] + adj[node[1]][v]:
            distance[v] = node[0] + adj[node[1]][v]
            heapq.heappush(queue, [distance[v], v])


for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])


# 자료구조 책 다익스트라 예제
'''
V = 7

adj = [[0, 7, 99, 99, 3, 10, 99], [7, 0, 4, 10, 2, 6, 99], [99, 4, 0, 2, 99, 99, 99], [99, 10, 2, 0, 11, 9, 4], [3, 2, 99, 11, 0, 99, 5], [1, 6, 99, 9, 99, 0, 99], [99, 99, 99, 4, 5, 99, 0]]

visited = [0] * V
distance = adj[0]
S = [0]
visited[0] = 1

for _ in range(V - 1):
    mini = 99
    for i in range(V):
        if visited[i] == 0 and distance[i] < mini:
            mini = distance[i]
    S.append(distance.index(mini))
    visited[distance.index(mini)] = 1
    print("S = ", S)
    for i in range(V):
        distance[i] = min(distance[i], distance[S[-1]] + adj[S[-1]][i])
    print("distance = ", distance)

print(distance)
'''