# 1D1P Day111 BOJ 10974번 모든 순열 문제 - 2021.02.23

N = int(input())

visited = [0] * (N+1)

def permutation(N, element, depth):
    if depth == N:
        print(*element)
        return
    
    for i in range(1, N+1):
        if visited[i] == 0:
            visited[i] = 1
            element.append(i)
            permutation(N, element, depth+1)
            visited[element.pop()] = 0

permutation(N, [], 0)