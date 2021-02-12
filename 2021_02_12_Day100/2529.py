# 1D1P Day100 BOJ 2529번 부등호 문제 - 2021.02.12
# 100일 축하!

K = int(input())
inqu = list(input().split())

answer = 0

Max = '0'
Min = '999999999'

def isitcorrect(numbers, inqu, K):

    global Max, Min

    result = 1
    for i in range(K):
        if inqu[i] == '<':
            if numbers[i] >= numbers[i+1]:
                result = 0
                return
        
        elif inqu[i] == '>':
            if numbers[i] <= numbers[i+1]:
                result = 0
                return

    if result:
        tmp = ""
        for num in numbers:
            tmp += str(num)

    if tmp > Max:
        Max = tmp
    if tmp < Min:
        Min = tmp
    
    return

def makenumbers(element, depth, visited, K):
    global answer

    if depth == K+1:
        isitcorrect(element, inqu, K)
        return
    
    for i in range(10):
        if visited[i] == 0:
            element.append(i)
            visited[i] = 1
            makenumbers(element, depth+1, visited, K)
            visited[element.pop()] = 0

visited = [0] * 10
makenumbers([], 0, visited, K)
print(Max)
print(Min)