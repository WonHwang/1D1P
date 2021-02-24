# 1D1P Day112 BOJ 15654번 N과 M (5) 문제 - 2021.02.24

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

def printnumber(element):
    for i in range(M):
        print(numbers[element[i]], end = ' ')
    print()

def back(element, depth):

    if depth == M:
        printnumber(element)
        return
    
    for i in range(N):
        if visited[i] == 0:
            element.append(i)
            visited[i] = 1
            back(element, depth + 1)
            visited[element.pop()] = 0

visited = [0] * N
back([], 0)