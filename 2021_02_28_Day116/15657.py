# 1D1P Day116 BOJ 15657번 N과 M (8) 문제 - 2021.02.28

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def dfs(element, depth):

    if depth == M:
        print(*element)
        return
    
    for num in numbers:
        if not element:
            element.append(num)
            dfs(element, depth+1)
            element.pop()

        elif element and num >= element[-1]:
            element.append(num)
            dfs(element, depth+1)
            element.pop()

dfs([], 0)