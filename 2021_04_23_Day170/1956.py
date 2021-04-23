# 1D1P Day170 BOJ 1956번 운동 문제 - 2021.04.23

from sys import stdin
import heapq
input = stdin.readline
INF = 10**9

V, E = map(int, input().split())

adj = [{} for _ in range(V+1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    adj[a][b] = w


answer_list = [INF] * (V+1)

for start in range(1, V+1):
    queue = []
    heapq.heappush(queue, (0, start))
    distance = [INF] * (V+1)
    distance[start] = 0

    while queue:
        node = heapq.heappop(queue)
        weight = node[0]

        for v in adj[node[1]]:
            if adj[node[1]][v] + weight < distance[v]:
                distance[v] = adj[node[1]][v] + weight
                heapq.heappush(queue, (distance[v], v))
    
    cycles = [INF] * (V+1)
    for i in range(1, V+1):
        if i != start:
            try:
                cycles[i] = distance[i] + adj[i][start]
            except:
                pass
    answer_list[start] = min(cycles)

answer = min(answer_list)

print(answer if answer != INF else -1)