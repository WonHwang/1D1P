# 1D1P Day80 SWEA 1219번 길찾기 문제 - 2021.01.23

from collections import deque

for _ in range(10):
    t, e = map(int, input().split())
    maps = [[] for i in range(100)]
    tmp = list(map(int, input().split()))
    for i in range(0, 2*e, 2):
        maps[tmp[i]].append(tmp[i+1])
    visited = [0] * 100
    queue = deque()
    queue.append(0)
    visited[0] = 1

    while queue:
        node = queue.popleft()
        if visited[99] == 1:
            break
        for v in maps[node]:
            if visited[v] == 0:
                queue.append(v)
                visited[v] = 1
    
    print(f"#{t} {visited[99]}")