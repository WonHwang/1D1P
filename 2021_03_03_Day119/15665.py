# 1D1P Day119 BOJ 15665번 N과 M (11) 문제 - 2021.03.03

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers = list(set(numbers))
numbers.sort()

element = []
def dfs(depth):

    if depth == M:
        print(*element)
        return
    
    for i in range(len(numbers)):
        element.append(numbers[i])
        dfs(depth + 1)
        element.pop()

dfs(0)