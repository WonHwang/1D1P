# 1D1P Day93 SWEA 1238번 Contact 문제 - 2021.02.05

from collections import deque

for t in range(1, 11):
    N, start = map(int, input().split())
    link = [[] for _ in range(N+1)]
    data = list(map(int, input().split()))

    for i in range(0, len(data), 2):
        link[data[i]].append(data[i+1])
    
    visited = [0] * (N+1)

    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.popleft()
        step = visited[node]

        for v in link[node]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = step + 1
    
    for i in range(N+1):
        if visited[i] == step:
            answer = i
    
    print(f"#{t} {answer}")