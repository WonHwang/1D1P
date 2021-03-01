# 1D1P Day117 BOJ 15663번 N과 M (9) 문제 - 2021.03.01

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

visited = [0] * N
answer = []

def dfs(element, depth):

    if depth == M:
        answer.append(element[:])
        return
        
    overlab = 0
    for i in range(N):
        if visited[i] == 0 and overlab != numbers[i]:
            element.append(numbers[i])
            overlab = numbers[i]
            visited[i] = 1
            dfs(element, depth + 1)
            element.pop()
            visited[i] = 0

dfs([], 0)
for ans in answer:
    print(*ans)