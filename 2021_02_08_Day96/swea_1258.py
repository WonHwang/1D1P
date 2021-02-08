# 1D1P Day96 SWEA 1258번 행렬 문제 - 2021.02.08

from collections import deque
for t in range(1, int(input())+1):
    N = int(input())
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))

    visited = [[0 for _ in range(N)] for __ in range(N)]

    result = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0 and visited[i][j] == 0:
                queue = deque()
                queue.append([i, j])
                visited[i][j] = 1

                while queue:
                    node = queue.popleft()
                    x, y = node[0], node[1]

                    if x < N-1 and visited[x+1][y] == 0 and matrix[x+1][y] != 0:
                        queue.append([x+1, y])
                        visited[x+1][y] = 1
                
                    if y < N- 1 and visited[x][y+1] == 0 and matrix[x][y+1] != 0:
                        queue.append([x, y+1])
                        visited[x][y+1] = 1
                
            
                result.append([x - i + 1, y - j + 1])

    result.sort(key = lambda x : x[0])
    result.sort(key = lambda x : x[0] * x[1])
    print(f"#{t}", end=" ")
    print(len(result), end=" ")
    for num in result:
        for n in num:
            print(n, end=" ")
    print()