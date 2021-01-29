# 1D1P Day86 programmers 그래프 1번 가장 먼 노드 문제 - 2021.01.29

from collections import deque

def solution(n, edge):
    info = [[] for _ in range(n+1)]
    
    for e in edge:
        x, y = e[0], e[1]
        info[x].append(y)
        info[y].append(x)
    
    
    visited = [0] * (n+1)
    queue = deque()
    queue.append(1)
    visited[1] = 1
    
    while queue:
        node = queue.popleft()
        step = visited[node]
        for v in info[node]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = step + 1
    
    maximum = max(visited)
    answer = 0
    for v in visited:
        if v == maximum:
            answer += 1
    return answer