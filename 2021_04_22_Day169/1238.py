# 1D1P Day169 BOJ 1238번 파티 문제 - 2021.04.22

import heapq

INF = 10**9

def dijkstra(start, N, X, option):

    queue = []
    heapq.heappush(queue, [0, start])
    distance = [INF] * (N+1)
    distance[start] = 0

    while queue:
        node = heapq.heappop(queue)

        for v in adj[node[1]]:
            if node[0] + adj[node[1]][v] < distance[v]:
                distance[v] = node[0] + adj[node[1]][v]
                heapq.heappush(queue, [distance[v], v])
    if option:
        return distance[X]
    
    else:
        return distance

N, M, X = map(int, input().split())

adj = [{} for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    adj[a][b] = w

for i in range(N):
    adj[i][i] = 0

answer = [0] * (N+1)
for i in range(1, N+1):
    if i == X:
        fromXtoOther = dijkstra(i, N, X, 0)
    
    else:
        answer[i] = dijkstra(i, N, X, 1)

for i in range(1, N+1):
    answer[i] += fromXtoOther[i]

print(max(answer[1:]))