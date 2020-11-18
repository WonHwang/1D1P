# 1D1P Day14 BOJ 11724번 연결 요소의 개수 문제 - 2020.11.18

import sys

def DFS(graph, node, visited, N):

    visited.append(node)

    for i in range(1, N+1):
        if graph[node][i] == 1 and i not in visited:
            DFS(graph, i, visited, N)
    
    return 1, visited

N, M = map(int, sys.stdin.readline().rstrip().split(' '))
graph = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[a][b] = 1

answer = 0
visited = []
for i in range(1, N+1):
    result, visited = DFS(graph, i, visited, N)
    answer += result

print(answer)