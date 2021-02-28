# 1D1P Day116 BOJ 15656번 N과 M (7) 문제 - 2021.02.28

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(element, depth):

    if depth == M:
        print(*element)
        return
    
    for num in numbers:
        element.append(num)
        dfs(element, depth+1)
        element.pop()

dfs([], 0)