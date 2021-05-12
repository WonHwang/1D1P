# 1D1P Day189 BOJ 18352번 특정 거리의 도시 찾기 문제 - 2021.05.12

from sys import stdin
from collections import deque
input = stdin.readline

N, M, K, X = map(int, input().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)

visited = [0] * (N+1)
queue = deque()
queue.append(X)
visited[X] = 1

while queue:
    node = queue.popleft()
    step = visited[node]

    for v in adj[node]:
        if visited[v] == 0:
            visited[v] = step + 1
            queue.append(v)

answer_list = []
for i in range(N+1):
    if visited[i] - 1 == K:
        answer_list.append(i)

if answer_list:
    for answer in answer_list:
        print(answer)

else:
    print(-1)