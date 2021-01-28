from sys import stdin
import heapq
input = stdin.readline
INF = 16000000000

N, E = map(int, input().split())
adj = [{} for _ in range(N+1)]

for _ in range(E):
    u, v, weight = map(int, input().split())
    adj[u][v] = weight
    adj[v][u] = weight

mustpoint = list(map(int, input().split()))

def dijkstra(start, end):
    distance = [INF] * (N+1)
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (0, start))

    while queue:
        node = heapq.heappop(queue)
        for v in adj[node[1]]:
            if distance[v] > node[0] + adj[node[1]][v]:
                distance[v] = node[0] + adj[node[1]][v]
                heapq.heappush(queue, (distance[v], v))
    return distance[end]

distance_of_two_point = dijkstra(mustpoint[0], mustpoint[1])
course1 = dijkstra(1, mustpoint[0]) + dijkstra(mustpoint[1], N) + distance_of_two_point
course2 = dijkstra(1, mustpoint[1]) + dijkstra(mustpoint[0], N) + distance_of_two_point

answer = course1 if course1 < course2 else course2

if answer < INF:
    print(answer)
else:
    print(-1)