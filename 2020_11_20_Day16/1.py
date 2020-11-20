# 1D1P Day16 Programmers DFS,BFS 2번 네트워크 문제 - 2020.11.20

def solution(n, computers):
    
    visited = [0] * n
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    def bfs(v):
        queue = []
        queue.append(v)
        visited[v] = 1
        while queue:
            node = queue.pop(0)
            for connection in graph[node]:
                if visited[connection] == 0:
                    queue.append(connection)
                    visited[connection] = 1
    
    answer = 0
    for i in range(n):
        if visited[i] == 0:
            bfs(i)
            answer += 1
    
    return answer