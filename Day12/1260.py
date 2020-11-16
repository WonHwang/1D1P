# 1D1P Day12 BOJ 1260번 DFS와 BFS 문제 - 2020.11.16

def DFS(graph, start, visited, N):
    
    visited.append(start)

    for i in range(1, N+1):
        if i == start or i in visited:
            continue
        elif graph[start][i] == 1:
            DFS(graph, i, visited, N)
    
    return visited

def BFS(graph, start, N):

    visited = []
    queue = []

    queue.append(start)

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            for i in range(1, N+1):
                if graph[node][i] == 1:
                    queue.append(i)

    return visited

N, M, V = map(int, input().split(' '))

graph = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(M):
    a, b = map(int, input().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

visited_DFS = DFS(graph, V, [], N)
visited_BFS = BFS(graph, V, N)

answer_DFS = ""
answer_BFS = ""

for node in visited_DFS:
    answer_DFS += str(node) + " "
for node in visited_BFS:
    answer_BFS += str(node) + " "

answer_DFS = answer_DFS[:-1]
answer_BFS = answer_BFS[:-1]

print(answer_DFS)
print(answer_BFS)