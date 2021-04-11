# 1D1P Day158 BOJ 1916번 최소비용 구하기 문제 - 2021.04.11

from sys import stdin
from collections import deque
input = stdin.readline
INF = 100000001

N = int(input())
M = int(input())

adj = [[INF for _ in range(N+1)] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    if adj[a][b] > c:
        adj[a][b] = c

for i in range(N+1):
    adj[i][i] = 0

start, end = map(int, input().rstrip().split())

queue = deque()
queue.append(start)
visited = [0] * (N+1)
visited[start] = 1
distance = adj[start][:]

while queue:
    node = queue.popleft()
    for i in range(N+1):
        distance[i] = min(distance[i], distance[node] + adj[node][i])
    
    Min = INF
    for i in range(N+1):
        if visited[i] == 0 and distance[i] < Min:
            Min = distance[i]
            idx = i
    
    if Min != INF:
        queue.append(idx)
        visited[idx] = 1

print(distance[end])