# 1D1P Day111 SWEA 1219번 길찾기 문제 - 2021.02.23

for tc in range(10):

    tc, N = map(int, input().split())
    info = list(map(int, input().split()))
    adj = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(0, len(info), 2):
        adj[info[i]][info[i+1]] = 1

    visited = [0] * 100

    def dfs(n):

        visited[n] = 1

        for v in range(100):
            if adj[n][v] == 1 and visited[v] == 0:
                dfs(v)
    
    dfs(0)
    answer = 1 if visited[99] == 1 else 0

    print(f"#{tc} {answer}")