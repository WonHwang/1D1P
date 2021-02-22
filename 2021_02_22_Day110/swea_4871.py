# 1D1P Day110 SWEA 4871번 그래프 경로 문제 - 2021.02.22

from collections import deque

for tc in range(1, int(input()) + 1):

    V, E = map(int, input().split())

    graph = [[0 for _ in range(V+1)] for _ in range(V+1)]

    info = [[] for _ in range(V+1)]

    for i in range(E):
        a, b = map(int, input().split())
        info[a].append(b)

    for i in range(1, V+1):
        queue = deque()
        visited = [0] * (V+1)
        queue.append(i)
        visited[i] = 1
        graph[i][i] = 1

        while queue:
            node = queue.popleft()
            for v in info[node]:
                if visited[v] == 0:
                    graph[i][v] = 1
                    visited[v] = 1
                    queue.append(v)
    
    s, g = map(int, input().split())
    print(f"#{tc} {graph[s][g]}")