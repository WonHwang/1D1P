# 1D1P Day168 SWEA 2814번 최장 경로 문제 - 2021.04.21

answer = 0

def dfs(node, N, depth):

    global answer

    if depth > answer:
        answer = depth

    for v in adj[node]:
        if visited[v] == 0:
            visited[v] = 1
            dfs(v, N, depth+1)
            visited[v] = 0

for tc in range(1, int(input())+1):

    N, M = map(int, input().split())

    adj = [[] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)
    
    answer = 0

    for i in range(1, N+1):
        visited = [0] * (N+1)
        dfs(i, N, 0)

    if not answer:
        answer = 1
    print(f"#{tc} {answer}")