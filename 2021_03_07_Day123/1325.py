# 1D1P Day123 BOJ 1325번 효율적인 해킹 문제 - 2021.03.07
# 둘다 pypy3

from sys import stdin
from collections import deque
input = stdin.readline

N, M = map(int, input().rstrip().split())

adj = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().rstrip().split())
    adj[b].append(a)

connections = [0] * (N+1)

def dfs(node, start):
    connections[start] += 1
    visited[node] = 1

    for v in adj[node]:
        if visited[v] == 0:
            dfs(v, start)

for i in range(1, N+1):
    visited = [0] * (N+1)
    dfs(i, i)

Max = max(connections)
for i in range(1, N+1):
    if connections[i] == Max:
        print(i, end = ' ')
print()

# from sys import stdin
# from collections import deque

# input = stdin.readline

# N, M = map(int, input().rstrip().split())
# connection = [[] for _ in range(N+1)]
# howmany = [0] * (N+1)
# for _ in range(M):
#     a, b = map(int, input().rstrip().split())
#     connection[b].append(a)

# for i in range(1, N+1):
#     if connection[i]:

#         visited = [0] * (N+1)
#         queue = deque()
#         queue.append(i)
#         visited[i] = 1
#         tmp = 0
#         while queue:
#             node = queue.popleft()
#             tmp += 1
            
#             for v in connection[node]:
#                 if visited[v] == 0:
#                     visited[v] = 1
#                     queue.append(v)
#         howmany[i] = tmp

# Max = max(howmany)
# answer = []
# for i in range(1, N+1):
#     if howmany[i] == Max:
#         answer.append(i)
# print(*answer)