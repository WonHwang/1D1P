# 1D1P Day118 BOJ 15664번 N과 M (10) 문제 - 2021.03.02

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * N
element = []
def dfs(depth):
    
    if depth == M:
        print(*element)
        return
    
    overlap = 0
    for i in range(depth, N):
        if not element:
            if numbers[i] != overlap:
                element.append(numbers[i])
                visited[i] = 1
                overlap = numbers[i]
                dfs(depth+1)
                element.pop()
                visited[i] = 0
        else:
            if numbers[i] >= element[-1] and visited[i] == 0 and numbers[i] != overlap:
                element.append(numbers[i])
                visited[i] = 1
                overlap = numbers[i]
                dfs(depth+1)
                element.pop()
                visited[i] = 0

dfs(0)