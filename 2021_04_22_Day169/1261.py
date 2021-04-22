# 1D1P Day169 BOJ 1261번 알고스팟 문제 - 2021.04.22

import heapq

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
INF = 10**9

def dijkstra(N, M):

    queue = []
    heapq.heappush(queue, [0, 0, 0])
    cost[0][0] = 0

    while queue:
        node = heapq.heappop(queue)
        weight, x, y = node[0], node[1], node[2]

        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if 0 <= a < N and 0 <= b < M:
                if weight + int(room[a][b]) < cost[a][b]:
                    cost[a][b] = weight + int(room[a][b])
                    heapq.heappush(queue, [cost[a][b], a, b])
    
    return cost[N-1][M-1]

M, N = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(input()))

cost = [[INF for _ in range(M)] for _ in range(N)]

print(dijkstra(N, M))