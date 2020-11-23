# 1D1P Day16 BOJ 10451번 순열 사이클 문제 - 2020.11.19

T = int(input())
for _ in range(T):
    
    N = int(input())
    array = input().split(' ')
    for i in range(N):
        array[i] = int(array[i])
    array = [0] + array

    visited = [0] * (N+1)
    
    def BFS(start):
        queue = [array[start]]
        while queue:
            node = queue.pop(0)
            visited[node] = 1
            queue.append(array[node])
            if start == node:
                return 1

    answer = 0
    for i in range(1, N+1):
        if visited[i] == 0:
            answer += BFS(i)
    
    print(answer)