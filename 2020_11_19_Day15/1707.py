# 1D1P Day15 BOJ 1707번 이분 그래프 문제 - 2020.11.19

import sys

K = int(input())

for i in range(K):
    
    V, E = map(int, sys.stdin.readline().rstrip().split(' '))
    graph = [[] for j in range(V+1)]
    for j in range(E):
        a, b = map(int, sys.stdin.readline().strip().split(' '))
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (V+1)

    def isbipartite(v):
        queue = [v]
        visited[v] = 1
        while queue:
            node = queue.pop(0)
            for next in graph[node]:
                if visited[next] == 0:
                    if visited[node] == 1:
                        visited[next] = 2
                    elif visited[node] == 2:
                        visited[next] = 1
                    queue.append(next)
                elif visited[next] == visited[node]:
                    return False
        return True

    for k in range(1, V+1):
        if visited[k] == 0:
            answer = isbipartite(k)
            if not answer:
                break

    if answer:
        print("YES")
    else:
        print("NO")